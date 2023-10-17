from django.db import models


class WordCount(models.Model):
    article = models.URLField()
    word = models.CharField(max_length=255)
    count = models.PositiveIntegerField()
    author = models.CharField(max_length=255, blank=True)
