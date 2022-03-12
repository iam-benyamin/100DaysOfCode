from django.urls import path

from .views import function_base_home, ClassBaseHome


urlpatterns = [
    path('function/view/', function_base_home),
    path('class/view/', ClassBaseHome.as_view()),
]
