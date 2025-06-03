from django.conf import settings
from django.core.validators import RegexValidator
from rest_framework import serializers


class RelatedModelField(serializers.PrimaryKeyRelatedField):
    serializer = None

    def __init__(self, serializer, **kwargs):
        self.serializer = serializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, obj):
        return self.serializer(obj).data
