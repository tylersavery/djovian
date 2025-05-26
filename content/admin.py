from admin_auto_filters.filters import AutocompleteFilterFactory
from django.contrib import admin

from admin.models import ModelAdmin
from .models import Example


@admin.register(Example)
class ExampleAdmin(ModelAdmin):
    list_display = (
        "title",
        "owner",
        "created_at",
    )
    list_filter = (AutocompleteFilterFactory("Owner", "owner"),)

    search_fields = ("title",)
    readonly_fields = (
        "uuid",
        "created_at",
        "updated_at",
    )

    autocomplete_fields = ("owner",)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("owner")

    fields = (
        "uuid",
        "title",
        "owner",
        "created_at",
        "updated_at",
    )
