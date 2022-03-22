from django.urls import path
from .views import user_registartion_view, home



urlpatterns = [
    path('', home),
    path('user_register/', user_registartion_view),
]