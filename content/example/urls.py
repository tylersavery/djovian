from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.ExampleListView.as_view(), name="example_list"),
    path("create/", views.ExampleEditView.as_view(), name="example_create"),
    path("<uuid:uuid>/", views.ExampleDetailView.as_view(), name="example_detail"),
    path("<uuid:uuid>/edit/", views.ExampleEditView.as_view(), name="example_edit"),
    path(
        "<uuid:uuid>/delete/", views.ExampleDeleteView.as_view(), name="example_delete"
    ),
    path(
        "actions/list/",
        views.ExampleListView.as_view(),
        {"inner_content": True},
        name="example_list_action",
    ),
]
