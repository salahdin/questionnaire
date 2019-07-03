from django.urls import path
from .import views

urlpatterns = [
    path('eligable/', views.eligability, name="eligability"),
]