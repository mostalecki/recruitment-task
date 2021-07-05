from rest_framework import serializers

from src.books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "publication_date",
            "page_count",
            "cover_url",
            "language",
            "isbn",
        ]
