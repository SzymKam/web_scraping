from django.db import models


class WordCount(models.Model):
    article = models.URLField()
    word = models.CharField(max_length=255)
    count = models.PositiveIntegerField()
    author = models.CharField(max_length=255, blank=True)
    author_lowercase = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"article: {self.article}, word: {self.word}"
