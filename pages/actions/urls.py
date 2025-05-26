from django.urls import path, include

from . import views

urlpatterns = [
    path(
        "example/",
        views.ExampleActionView.as_view(),
        name="example_action",
    ),
]
