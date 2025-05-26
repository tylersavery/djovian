from project.settings.environment import ENV


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = ENV.bool("EMAIL_USE_TLS", default=True)
EMAIL_PORT = ENV.str("EMAIL_PORT", default=587)

EMAIL_HOST = ENV.str("EMAIL_HOST")
EMAIL_HOST_USER = ENV.str("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = ENV.str("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = ENV.str("DEFAULT_FROM_EMAIL")
