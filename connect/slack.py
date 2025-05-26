import requests
from django.conf import settings


def send_slack_notification(message: str, url=None, url_label=None):

    if settings.SLACK_NOTIFICATION_WEBHOOK:
        text = message
        if url and url_label:
            text = f"{message}\n<{url}|{url_label}>"
        elif url:
            text = f"{message}\n<{url}>"

        requests.post(
            (settings.SLACK_NOTIFICATION_WEBHOOK),
            json={"text": text},
        )
