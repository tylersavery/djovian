# views/debug_errors.py

from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponseNotFound


def debug_404(request):
    return HttpResponseNotFound(render(request, "404.html"))


def debug_500(request):
    return HttpResponseServerError(render(request, "500.html"))
