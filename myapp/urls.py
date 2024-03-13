# myapp/urls.py

from django.urls import path
from .views import Home, About, Llamas, Cats  # Import class-based views

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("about/", About.as_view(), name="about"),
    path("llamas/", Llamas.as_view(), name="llamas"),
    path("cats/", Cats.as_view(), name="cats"), 
 
]
