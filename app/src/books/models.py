from django.db import models

from src.books.enums import Language
from src.books.validators import isbn_validator


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    page_count = models.PositiveIntegerField(null=True, blank=True)
    cover_url = models.URLField(null=True, blank=True)
    language = models.CharField(max_length=32, choices=Language.choices, null=True, blank=True)
    isbn = models.CharField(
        verbose_name="ISBN", max_length=32, null=True, blank=True, validators=[isbn_validator]
    )
    # volume_id is used when fetching books from Google Books API
    volume_id = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
