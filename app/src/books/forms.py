from django.forms import ModelForm

from src.books.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "publication_date",
            "page_count",
            "cover_url",
            "language",
            "isbn",
        ]
