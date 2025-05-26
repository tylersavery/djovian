from admin_auto_filters.filters import AutocompleteFilterFactory
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from admin.models import ModelAdmin

# from .models import CommentReport


# @admin.register(CommentReport)
# class CommentReportAdmin(ModelAdmin):

#     search_fields = ["email"]
#     readonly_fields = ["created_at", "uuid"]
#     autocomplete_fields = ["comment"]
#     list_filter = [
#         AutocompleteFilterFactory(_("Owner"), "owner"),
#         AutocompleteFilterFactory(_("Comment"), "comment"),
#     ]

#     list_display = [
#         "reason",
#         "comment",
#         "owner",
#         "created_at",
#     ]

#     date_hierarchy = "created_at"
#     ordering = ["-created_at"]

#     fieldsets = (
#         (
#             _("Details"),
#             {
#                 "fields": [
#                     "comment",
#                     "reason",
#                     "description",
#                     "owner",
#                     "email",
#                     "created_at",
#                 ]
#             },
#         ),
#     )
