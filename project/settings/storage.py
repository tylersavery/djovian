from project.settings.environment import ENV
from .debug import DEBUG
from .aws import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_STORAGE_BUCKET_NAME,
    AWS_DEFAULT_REGION,
    USE_S3_FOR_STATIC_FILES,
)

# https://whitenoise.readthedocs.io/en/latest/django.html
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "access_key": AWS_ACCESS_KEY_ID,
            "secret_key": AWS_SECRET_ACCESS_KEY,
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "region_name": AWS_DEFAULT_REGION,
        },
    },
    "staticfiles": (
        {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "access_key": AWS_ACCESS_KEY_ID,
                "secret_key": AWS_SECRET_ACCESS_KEY,
                "bucket_name": AWS_STORAGE_BUCKET_NAME,
                "region_name": AWS_DEFAULT_REGION,
            },
        }
        if USE_S3_FOR_STATIC_FILES
        else {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        }
    ),
}


AWS_DEFAULT_ACL = "public-read"
AWS_QUERYSTRING_AUTH = False


TEMP_DIR = ENV.str("TEMP_DIR", "/tmp")
