from content.example.forms import ExampleForm
from pages.base_view import BaseView
from django.shortcuts import get_object_or_404, redirect
from content.example.models import Example
from django.core.paginator import Paginator

from project import settings


class ExampleListView(BaseView):

    def get_template_names(self) -> list[str]:
        if self.kwargs.get("inner_content", False):
            return "example/partials/_example_list_action.html"
        return "example/example_list.html"

    def get_item_list_context(self):
        page = int(self.request.GET.get("page") or 1)
        items = Example.objects.all().order_by("-created_at")
        paginator = Paginator(items, settings.API_DEFAULT_LIMIT)

        page_data = paginator.get_page(page)

        data = {
            "items": page_data,
            "page": page,
            "has_next": page_data.has_next(),
        }

        return data

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context |= self.get_item_list_context()
        return self.render_to_response(context)


class ExampleDetailView(BaseView):

    template_name = "example/example_detail.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        item = get_object_or_404(Example, uuid=kwargs["uuid"])

        context["is_owner"] = item.owner.id == request.user.id
        context["item"] = item

        return self.render_to_response(context)


class ExampleEditView(BaseView):

    template_name = "example/example_edit.html"

    def get_context_data(self, **context):
        context = super().get_context_data(**context)
        item_uuid = self.kwargs.get("uuid", None)
        if item_uuid:
            item = get_object_or_404(Example, uuid=item_uuid)
            if item.owner.id != self.request.user.id:
                raise Exception()
        else:
            item = Example(title="", owner=self.request.user)

        context["item"] = item
        context["form"] = ExampleForm(instance=item)

        return context

    def get(self, request, *args, **kwargs):
        try:
            context = self.get_context_data(**kwargs)
        except Exception:
            return redirect("example_list")

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        form = ExampleForm(request.POST, request.FILES, instance=context["item"])
        context["form"] = form

        if form.is_valid():
            item = form.save()
            return redirect("example_detail", uuid=item.uuid)

        return self.render_to_response(context)


class ExampleDeleteView(BaseView):

    template_name = "example/example_delete.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        item = get_object_or_404(Example, uuid=kwargs["uuid"])

        context["item"] = item

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        item = get_object_or_404(Example, uuid=context["uuid"])
        if item.owner.id != self.request.user.id:
            return redirect("example_list")

        item.delete()

        return redirect("example_list")
