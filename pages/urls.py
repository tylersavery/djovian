from django.urls import path, include

from . import views
from . import debug_views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("auth-required/", views.AuthRequiredPageView.as_view(), name="auth_required"),
    path(
        "contact/",
        views.ContactPageView.as_view(),
        name="contact",
    ),
    path(
        "faq/",
        views.FaqPageView.as_view(),
        name="faq",
    ),
    path(
        "create-stripe-checkout/success/",
        views.CreateStripeCheckoutSuccessView.as_view(),
        name="create_stripe_checkout_success",
    ),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path(
        "profile/<str:username>/",
        views.ProfileView.as_view(),
        name="profile",
    ),
    path("settings/", views.SettingsView.as_view(), name="settings"),
    path(
        "terms-of-service/",
        views.RedirectView.as_view(),
        name="terms_and_conditions",
        kwargs={
            "url": "https://app.termly.io/policy-viewer/policy.html?policyUUID=7a87d723-6ed5-4a85-b3f9-e0781c4ea692"
        },
    ),
    path(
        "privacy-policy/",
        views.RedirectView.as_view(),
        name="privacy_policy",
        kwargs={
            "url": "https://app.termly.io/policy-viewer/policy.html?policyUUID=dad71bd8-1064-4a84-8a8c-da89630f4bbd"
        },
    ),
    path(
        "cookie-policy/",
        views.RedirectView.as_view(),
        name="cookie_policy",
        kwargs={
            "url": "https://app.termly.io/policy-viewer/policy.html?policyUUID=12b6ed65-20c3-44d7-812a-ddfb0f150402"
        },
    ),
    path("example/", include("content.example.urls")),
]
