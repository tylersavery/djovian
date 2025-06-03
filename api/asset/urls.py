from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.InitUploadView.as_view(), name="init_asset_upload"),
]
