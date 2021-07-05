from django import forms

from src.books.models import Book


class BookForm(forms.ModelForm):
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


class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=128, required=False, label="Keywords")
