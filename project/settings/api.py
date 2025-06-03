from project.settings.environment import ENV

API_ENABLED = ENV.bool("API_ENABLED", default=True)
API_THROTTLE_ENABLED = ENV.bool("API_THROTTLE_ENABLED", default=False)
API_DEFAULT_LIMIT = ENV.int("API_DEFAULT_LIMIT", default=10)
API_MAX_LIMIT = ENV.int("API_MAX_LIMIT", default=100)
SWAGGER_ENABLED = ENV.bool("SWAGGER_ENABLED", default=True)


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "api.filters.ReversibleOrderingFilter",
        "rest_framework.filters.SearchFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_THROTTLE_CLASSES": [
        "api.throttling.AnonRateThrottle",
        "api.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": ENV.str("API_THROTTLE_RATE_ANON", default="300/min"),
        "user": ENV.str("API_THROTTLE_RATE_USER", default="300/min"),
    },
    "URL_FORMAT_OVERRIDE": None,
    "COERCE_DECIMAL_TO_STRING": False,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
