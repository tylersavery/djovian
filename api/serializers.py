from rest_framework import serializers
from django.utils.module_loading import import_string
from django.utils.functional import cached_property
from rest_framework.serializers import RelatedField


class ReadOnlyModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        setattr(self.Meta, "read_only_fields", [*self.fields])


class DynamicRelatedField(RelatedField):
    def __init__(self, serializer_path=None, **kwargs):
        assert (
            serializer_path is not None
        ), "The `serializer_path` argument is required."
        assert kwargs[
            "read_only"
        ], "Only readonly fields are supported for DynamicRelatedField"
        self.serializer_path = serializer_path
        super().__init__(**kwargs)

    @cached_property
    def serializer_object(self):
        serializer_class = import_string(self.serializer_path)
        return serializer_class()

    def to_representation(self, obj):
        return self.serializer_object.to_representation(obj)

    def to_internal_value(self, data):
        return None
