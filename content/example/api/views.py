from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)

from api.permissions import AllowAny, IsAuthenticated, IsOwner

from .querysets import ALL_EXAMPLES_QUERYSET
from .serializers import ExampleSerializer
from .filters import ExampleFilter


class ExampleAPIView(GenericAPIView):
    queryset = ALL_EXAMPLES_QUERYSET
    serializer_class = ExampleSerializer
    permission_classes = [AllowAny]
    filterset_class = ExampleFilter

    search_fields = ["title"]
    ordering = ["-created_at"]


class ExampleListCreateView(ListModelMixin, CreateModelMixin, ExampleAPIView):

    def get_permissions(self):
        method = self.request.method
        if method == "POST":
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ExampleRetrieveUpdateDestroy(
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ExampleAPIView
):
    def get_permissions(self):
        method = self.request.method
        if method != "GET":
            self.permission_classes = [IsOwner]
        return super().get_permissions()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
