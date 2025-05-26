import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from system.models import StripeWebhookEvent

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    StripeWebhookEvent.objects.get_or_create(
        event_id=event["id"],
        defaults={
            "event_type": event["type"],
            "payload": event,
        },
    )

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        metadata = session["metadata"]

    return HttpResponse(status=200)
