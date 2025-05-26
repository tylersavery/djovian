from django.shortcuts import get_object_or_404, render

from blog.models import BlogPostPage, Comment
from pages.base_view import BaseView


class ActionView(BaseView):
    pass


class ExampleActionView(ActionView):

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)

        if request.user.is_authenticated:
            owner = request.user

        return render(request, "partials/example/example.html", context)
