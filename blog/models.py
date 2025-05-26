from typing import Any

from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from django.conf import settings

from access.models import User


@register_snippet
class BlogTag(TaggedItemBase):
    content_object = ParentalKey(
        "BlogPostPage",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.tag.name


def get_context_data(request, kwargs) -> dict[str, Any]:

    user = request.user

    kwargs["authenticated_user"] = user if not user.is_anonymous else None
    kwargs["url_path"] = request.get_full_path()
    kwargs["release_version"] = settings.VERSION

    return kwargs


class BlogPostPage(Page):

    date = models.DateField("Post date")
    thumbnail = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    excerpt = models.TextField(blank=True)
    content = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogTag, blank=True)

    comments_enabled = models.BooleanField(default=True)

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("thumbnail"),
        FieldPanel("excerpt"),
        FieldPanel("content"),
        FieldPanel("tags"),
        FieldPanel("comments_enabled"),
    ]

    parent_page_types = ["blog.BlogListPage"]
    subpage_types = []

    def user_has_comment_access(self, request):

        user = request.user

        if not user.is_authenticated:
            return False

        if not self.comments_enabled:
            return False

        return True

    def get_context(self, request):
        context = super().get_context(request)
        context = get_context_data(request, context)

        context["can_comment"] = self.user_has_comment_access(request)
        context["comments"] = Comment.objects.filter(blog_post=self)

        return context

    def serve(self, request):

        can_access = can_access_blog_post(self, request.user)

        if not can_access:
            return redirect(reverse("home"))

        return super().serve(request)

    class Meta:
        ordering = ["-date"]


class BlogListPage(Page):

    content_panels = Page.content_panels + []

    subpage_types = ["blog.BlogPostPage"]

    def get_context(self, request):
        context = super().get_context(request)
        context = get_context_data(request, context)
        context["posts"] = BlogPostPage.objects.live().specific().order_by("-date")

        return context


class Comment(models.Model):
    blog_post = models.ForeignKey(
        BlogPostPage, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
