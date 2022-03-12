from importlib.resources import path
from django.shortcuts import render

from django.views import View
from django.views.generic.base import TemplateView



def function_base_home(request):
    return render(request, "function_base_home.html")


class ClassBaseHome(TemplateView):
    template_name = "class_base_home.html"

