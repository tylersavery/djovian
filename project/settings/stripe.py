from project.settings.environment import ENV


STRIPE_PUBLISHABLE_KEY = ENV.str("STRIPE_PUBLISHABLE_KEY")
STRIPE_SECRET_KEY = ENV.str("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = ENV.str("STRIPE_WEBHOOK_SECRET")
