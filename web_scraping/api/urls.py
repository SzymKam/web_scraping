from django.urls import path

from .views.authors import AuthorListView
from .views.top_10_by_author import Top10ByAuthorView
from .views.top_10_view import Top10View

urlpatterns = [
    path("stats/", Top10View.as_view(), name="top-10-words"),
    path("stats/<str:author>/", Top10ByAuthorView.as_view(), name="word-counts-by-author"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
]
