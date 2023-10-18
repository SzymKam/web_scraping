import re
from collections import Counter

import nltk
import requests
from bs4 import BeautifulSoup
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from nltk.corpus import stopwords

from ..constans import BASE_URL
from ..models import WordCount


def save_words_to_db(article, urls_with_author):
    response = requests.get(BASE_URL + article)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    words = re.findall(r"\w+", text)
    words = [word.lower() for word in words]

    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))

    filtered_words = [word for word in words if word not in stop_words]

    word_frequency = Counter(filtered_words)

    author = urls_with_author.get(article)
    author_lowercase = author.replace(" ", "").lower()

    for word, count in word_frequency.items():
        try:
            existing_article = get_object_or_404(klass=WordCount, article=article, word=word)
            if existing_article:
                existing_article.count = count
                existing_article.author = author
                existing_article.author_lowercase = author_lowercase
                existing_article.save()
                print(f"{existing_article} updated!")

        except Http404:
            new_article = WordCount.objects.create(
                article=article, word=word, count=count, author=author, author_lowercase=author_lowercase
            )
            new_article.save()
            print(f"{new_article} created")
