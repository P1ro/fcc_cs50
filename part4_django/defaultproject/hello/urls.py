from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("p1ro", views.p1ro, name="p1ro")
]