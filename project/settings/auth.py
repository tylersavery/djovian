# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
from project.settings.environment import USE_SSL


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = "access.User"

# django-allauth config
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "home"

LOGIN_URL = "/auth/login"

# https://django-allauth.readthedocs.io/en/latest/views.html#logout-account-logout
ACCOUNT_LOGOUT_REDIRECT_URL = "home"

# https://django-allauth.readthedocs.io/en/latest/installation.html?highlight=backends
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True


if USE_SSL:
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ACCOUNT_FORMS = {
    "add_email": "allauth.account.forms.AddEmailForm",
    "change_password": "allauth.account.forms.ChangePasswordForm",
    "confirm_login_code": "allauth.account.forms.ConfirmLoginCodeForm",
    "login": "allauth.account.forms.LoginForm",
    "request_login_code": "allauth.account.forms.RequestLoginCodeForm",
    "reset_password": "allauth.account.forms.ResetPasswordForm",
    "reset_password_from_key": "allauth.account.forms.ResetPasswordKeyForm",
    "set_password": "allauth.account.forms.SetPasswordForm",
    "signup": "access.forms.CustomSignupForm",
    "user_token": "allauth.account.forms.UserTokenForm",
}

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "FETCH_USERINFO": True,
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,
    }
}
