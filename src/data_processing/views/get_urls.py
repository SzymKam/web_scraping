from http import HTTPStatus

import requests
from bs4 import BeautifulSoup


def return_urls(base_url: str) -> dict:
    articles_check = []
    articles_and_authors = {}
    response = requests.get(base_url)
    if response.status_code == HTTPStatus.OK:
        soup = BeautifulSoup(response.text, "html.parser")

    article_links = soup.find_all("article", class_="post-card")

    for article in article_links:
        link = article.find("a", class_="title")["href"]
        author = article.find("span", class_="author").find("a").text

        if link not in articles_check:
            articles_check.append(link)
            articles_and_authors.update({link: author})
    return articles_and_authors
