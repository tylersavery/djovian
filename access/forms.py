from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from allauth.account.forms import SignupForm, PasswordField
from allauth.utils import set_form_field_order
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _, pgettext

from django.conf import settings


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            "bio",
            "avatar",
        )


class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields["password1"] = PasswordField(
            label=_("Password"),
            autocomplete="new-password",
            # help_text=password_validation.password_validators_help_text_html(),
        )
        if settings.ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE:
            self.fields["password2"] = PasswordField(
                label=_("Confirm Password"), autocomplete="new-password"
            )

        if hasattr(self, "field_order"):
            set_form_field_order(self, self.field_order)


class SettingsForm(forms.Form):

    bio = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}), label="Bio", required=False
    )
    avatar_key = forms.CharField(widget=forms.HiddenInput, required=False)
    address_1 = forms.CharField(required=False, label="Address")
    address_2 = forms.CharField(required=False, label="Address 2")
    city = forms.CharField(required=False, label="City")
    state = forms.CharField(required=False, label="State")
    country = forms.CharField(required=False, label="Country")
    zipcode = forms.CharField(required=False, label="Zipcode")
