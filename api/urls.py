from django.urls import include, path


urlpatterns = [
    path("webhooks/", include("api.webhooks.urls")),
]
