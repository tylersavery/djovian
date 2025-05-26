from django.conf import settings


def global_context(request):
    context = {}
    if settings.GTAG_ID:
        context["gtag_id"] = settings.GTAG_ID

    return context
