# myapp/urls.py

from django.urls import path

from . import views

# This style is used for class view: views.classname.as_view()

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("about/", views.About.as_view(), name="about"),
    path("llamas/", views.Llamas.as_view(), name="llamas"),
    path("cats/", views.Cats.as_view(), name="cats"),
    path('theme/', views.ThemeView.as_view(), name='theme'),
]
