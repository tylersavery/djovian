from django.urls import include, path


urlpatterns = [
    path("access/", include("access.api.urls")),
    path("example/", include("content.api.urls")),
    path("webhooks/", include("api.webhooks.urls")),
]
