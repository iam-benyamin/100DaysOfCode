from django.urls import path

from .views import home, static

urlpatterns = [
    path('/', home),
    path('static/', static),
]
