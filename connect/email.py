from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags


def send_email(
    subject, body, recipients, from_email=settings.DEFAULT_FROM_EMAIL, text_body=None
):
    if isinstance(recipients, str):
        recipients = (recipients,)

    if len(recipients) < 1:
        return

    send_mail(
        subject,
        strip_tags(text_body or body),
        from_email,
        recipients,
        html_message=body,
        fail_silently=False,
    )
