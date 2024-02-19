from django.shortcuts import HttpResponse, redirect, render
from django.views.generic import View

from ..constants import URL_TO_GET_ARTICLES
from ..models import WordCount
from .get_urls import return_urls
from .get_words import save_words_to_db


class InitialView(View):
    def get(self, request) -> HttpResponse:
        self.update_db()
        return redirect("main_view")

    def update_db(self) -> None:
        urls_with_author = return_urls(base_url=URL_TO_GET_ARTICLES)
        for article in urls_with_author:
            save_words_to_db(article=article, urls_with_author=urls_with_author)
        print("Database updated!")


class MainView(View):
    def get(self, request) -> HttpResponse:
        authors = WordCount.objects.values("author", "author_lowercase").distinct()

        return render(request, template_name="data_processing/main-template.html", context={"authors": authors})
