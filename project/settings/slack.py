from project.settings.environment import ENV


SLACK_NOTIFICATION_WEBHOOK = ENV.str("SLACK_NOTIFICATION_WEBHOOK", default=None)
