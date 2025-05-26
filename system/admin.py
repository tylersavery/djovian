from django.contrib import admin

from system.models import StripeWebhookEvent
from admin.models import ModelAdmin

# Register your models here.


@admin.register(StripeWebhookEvent)
class StripeWebhookEventAdmin(ModelAdmin):
    list_display = ("event_id", "event_type", "received_at")
    search_fields = ("event_id", "event_type")
    readonly_fields = ("event_id", "event_type", "payload", "received_at")
