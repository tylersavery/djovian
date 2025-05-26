import os
from project.settings.environment import ENV
from .environment import BASE_DIR
from .debug import DEBUG
from .aws import AWS_STORAGE_BUCKET_NAME, USE_S3_FOR_STATIC_FILES
from shutil import which

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = None if USE_S3_FOR_STATIC_FILES else os.path.join(BASE_DIR, "staticfiles")

# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = (
    f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/"
    if USE_S3_FOR_STATIC_FILES
    else "/static/"
)


# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "theme", "static"),
    os.path.join(BASE_DIR, "static"),
]


NPM_BIN_PATH = which("npm")
