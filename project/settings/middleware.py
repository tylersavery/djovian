from .debug import DEBUG, LIVE_RELOAD

# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # WhiteNoise
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",  # Django Debug Toolbar
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",  # django-allauth
    # "django_browser_reload.middleware.BrowserReloadMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

if DEBUG and LIVE_RELOAD:
    MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")
