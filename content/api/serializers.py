from rest_framework import serializers

from access.api.querysets import ALL_USERS_QUERYSET
from access.api.serializers import PublicUserSerializer
from content.models import Example
from api.fields import RelatedModelField


class ExampleSerializer(serializers.ModelSerializer):

    owner = RelatedModelField(
        PublicUserSerializer, queryset=ALL_USERS_QUERYSET, many=False, required=False
    )

    class Meta:
        model = Example
        fields = [
            "id",
            "uuid",
            "title",
            "description",
            "image",
            "owner",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "uuid",
            "owner",
            "created_at",
        ]
