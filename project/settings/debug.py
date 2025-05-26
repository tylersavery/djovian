from project.settings.environment import ENV

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = ENV.bool("DEBUG", False)


# django-debug-toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# https://docs.djangoproject.com/en/dev/ref/settings/#internal-ips
INTERNAL_IPS = [
    "127.0.0.1",
    "0.0.0.0",
]


# DEBUG_TOOLBAR_CONFIG = {
#     "SHOW_TOOLBAR_CALLBACK": lambda r: False,
# }

LIVE_RELOAD = True
