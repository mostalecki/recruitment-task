from django.db import models

from src.books.enums import Language
from src.books.validators import isbn_validator


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256, null=True, blank=True)
    publication_date = models.DateField()
    page_count = models.PositiveIntegerField()
    cover_url = models.URLField()
    language = models.CharField(max_length=32, choices=Language.choices)
    isbn = models.CharField(
        max_length=13, null=True, blank=True, validators=[isbn_validator]
    )