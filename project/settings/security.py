from project.settings.environment import ENV

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ENV.list("ALLOWED_HOSTS")

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV.str("SECRET_KEY")

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = []
