from django.urls import include, path

from access.api.views import TokenCreateView, TokenRefreshView

urlpatterns = [
    path("token/", TokenCreateView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
