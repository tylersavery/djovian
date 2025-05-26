import base64
from typing import Any
import uuid
from django.views.generic import TemplateView
from django.conf import settings
from django.core.files.base import ContentFile
from datetime import datetime


class BaseView(TemplateView):

    seo_title_suffix = None
    seo_description_override = None
    seo_image_url_override = None

    def get_context_data(self, **context: Any) -> dict[str, Any]:

        user = self.request.user

        context["authenticated_user"] = user if not user.is_anonymous else None
        context["url_path"] = self.request.get_full_path()
        context["release_version"] = settings.VERSION
        context["current_year"] = datetime.now().year
        context["support_email"] = settings.SUPPORT_EMAIL
        context["website_name"] = settings.WEBSITE_NAME

        context["seo"] = {
            "image": self.seo_image_url_override
            or f"{settings.FRONTEND_BASE_URL}/og.jpg",
            "title": (
                f"{settings.WEBSITE_NAME}: {self.seo_title_suffix}"
                if self.seo_title_suffix
                else settings.WEBSITE_NAME
            ),
            "description": self.seo_description_override or "",
            "keywords": "",
        }

        return super().get_context_data(**context)

    def handle_b64_image(self, data) -> ContentFile:
        format, imgstr = data.split(";base64,")
        ext = format.split("/")[-1]
        file_name = f"{uuid.uuid4()}.{ext}"
        image_data = base64.b64decode(imgstr)

        return ContentFile(image_data, name=file_name)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)
