from api import filters
from content.models import Example


class ExampleFilter(filters.FilterSet):
    is_featured = filters.BooleanFilter(field_name="is_featured")

    class Meta:
        model = Example
        fields = [
            "is_featured",
        ]
