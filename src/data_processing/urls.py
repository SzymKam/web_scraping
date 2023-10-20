from django.urls import path

from .views.main_view import InitialView, MainView

urlpatterns = [
    path("", InitialView.as_view(), name="initial-view"),
    path("main/", MainView.as_view(), name="main_view"),
]
