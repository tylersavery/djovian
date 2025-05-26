import os
from django.conf import settings
from django.urls import path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    path("auth/", include("allauth.urls")),
    path("cms/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("blog/", include(wagtail_urls)),
    path("api/", include("api.urls")),
    path("", include("pages.urls")),
]

if settings.ADMIN_ENABLED:
    urlpatterns.append(path(settings.ADMIN_URL_PATH, include("admin.urls")))

if settings.DEBUG and settings.LIVE_RELOAD:
    # import debug_toolbar

    # urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
    urlpatterns.append(path("__reload__/", include("django_browser_reload.urls")))
