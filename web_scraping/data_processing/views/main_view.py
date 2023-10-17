from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django.views.generic import View

from ..constans import URL_TO_GET_ARTICLES
from .get_urls import return_urls
from .get_words import save_words_to_db


class MainView(View):
    def get(self, request) -> HttpResponse:
        self.update_db()
        return HttpResponse("main view")

    def update_db(self) -> None:
        urls_with_author = return_urls(base_url=URL_TO_GET_ARTICLES)
        for article in urls_with_author:
            save_words_to_db(article=article, urls_with_author=urls_with_author)
        print("Database updated!")
