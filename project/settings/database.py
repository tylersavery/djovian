import dj_database_url

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {"default": dj_database_url.config()}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
