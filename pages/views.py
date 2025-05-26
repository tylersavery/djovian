from decimal import Decimal
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.db.models import Sum
import stripe
from access.forms import SettingsForm
from access.models import User

from content.models import Example
from pages.base_view import BaseView
from django.contrib.auth.models import AnonymousUser
from django.views.generic import TemplateView
from django.contrib import messages


stripe.api_key = settings.STRIPE_SECRET_KEY


class HomePageView(BaseView):
    template_name = "pages/home.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context["foo"] = "bar"

        return self.render_to_response(context)


class AuthRequiredPageView(BaseView):
    template_name = "pages/auth_required.html"


class ContactPageView(BaseView):
    template_name = "pages/contact.html"
    seo_title_suffix = "Contact"


class FaqPageView(BaseView):
    template_name = "pages/faq.html"
    seo_title_suffix = "FAQ"

    def get(self, request, *args, **kwargs):
        from pages.data.faq_data import faq_items

        context = self.get_context_data(**kwargs)
        context["faq_items"] = faq_items

        return self.render_to_response(context)


class AboutPageView(BaseView):
    template_name = "pages/about.html"


class ProfileView(BaseView):
    template_name = "pages/profile.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        user = get_object_or_404(User, username=kwargs["username"])

        context["user"] = user
        context["is_me"] = (
            request.user.id == user.id if request.user.is_authenticated else False
        )

        context["seo"]["title"] += f": {user.username}'s Profile"
        if user.bio:
            context["seo"]["description"] = user.bio

        return self.render_to_response(context)


class SettingsView(BaseView):

    template_name = "pages/settings.html"

    def get(self, request, *args, **kwargs):
        if not request.user or isinstance(request.user, AnonymousUser):
            return redirect("home")

        context = self.get_context_data(**kwargs)

        context["form"] = SettingsForm(
            {
                "bio": request.user.bio,
                "address_1": request.user.address_1,
                "address_2": request.user.address_2,
                "city": request.user.city,
                "state": request.user.state,
                "country": request.user.country,
                "zipcode": request.user.zipcode,
            }
        )

        context["avatar"] = request.user.avatar
        context["user"] = request.user

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["avatar"] = request.user.avatar

        user = request.user

        if not user or isinstance(user, AnonymousUser):
            messages.error(request, "You are not signed in!")
            return redirect("account_login")

        form = SettingsForm(request.POST, request.FILES)
        if form.is_valid():

            user.bio = form.cleaned_data["bio"]
            user.address_1 = form.cleaned_data["address_1"]
            user.address_2 = form.cleaned_data["address_2"]
            user.city = form.cleaned_data["city"]
            user.state = form.cleaned_data["state"]
            user.country = form.cleaned_data["country"]
            user.zipcode = form.cleaned_data["zipcode"]
            avatar_base64 = form.cleaned_data["avatar_base64"]
            if avatar_base64:
                user.avatar = self.handle_b64_image(avatar_base64)

            user.save()

            messages.success(request, "Profile updated")
            return redirect(reverse("settings"))

        context["form"] = form
        messages.warning(request, "There are some errors with your changes.")
        return self.render_to_response(context)


class TermsAndConditionsView(BaseView):
    template_name = "pages/terms_and_conditions.html"


class PrivacyPolicyView(BaseView):
    template_name = "pages/privacy_policy.html"


class CreateStripeCheckoutView(TemplateView):

    def post(self, request, *args, **kwargs):

        user = request.user
        amount = Decimal(request.POST.get("amount"))

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": f" Paymant",
                        },
                        "unit_amount": int(amount * Decimal(100)),  # in cents
                    },
                    "quantity": 1,
                }
            ],
            customer_email=user.email if user.is_authenticated else None,
            metadata={"user_id": str(user.id), "foo": "bar"},
            success_url=request.build_absolute_uri(
                reverse("create_stripe_checkout_success")
            ),
            cancel_url=request.build_absolute_uri(reverse("project_detail")),
        )

        return JsonResponse({"id": session.id})


class CreateStripeCheckoutSuccessView(BaseView):
    template_name = "pages/stripe_checkout_success.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)


class RedirectView(TemplateView):

    def get(self, request, *args, **kwargs):

        url = kwargs.get("url", None)
        if url:
            return redirect(url)

        return redirect("/")
