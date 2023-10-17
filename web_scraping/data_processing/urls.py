from django.urls import path

from .views.main_view import MainView

urlpatterns = [
    path("", MainView.as_view(), name="main-view"),
]
