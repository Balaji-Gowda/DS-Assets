from . import views
from django.urls import path

urlpatterns = [
    path("", views.display, name="display"),
    path("display", views.display, name="display")
]
