import os

from django.contrib.messages import constants as message_constants
from .environment import BASE_DIR

from .debug import DEBUG

# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "OPTIONS": {
            "loaders": [
                "apptemplates.Loader",
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "system.context_processors.global_context",
            ],
        },
    },
]


MESSAGE_LEVEL = message_constants.DEBUG if DEBUG else message_constants.INFO
