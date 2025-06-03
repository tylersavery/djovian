from django.urls import path
from .views import ExampleListCreateView, ExampleRetrieveUpdateDestroy

urlpatterns = [
    path("", ExampleListCreateView.as_view()),
    path("<uuid:uuid>/", ExampleRetrieveUpdateDestroy.as_view()),
]
