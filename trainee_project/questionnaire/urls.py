from django.urls import path
from .import views

urlpatterns = [
    path('', views.eligability, name="eligability"),
]