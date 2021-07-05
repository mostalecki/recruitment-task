from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView

from src.books.filters import BookFilter
from src.books.models import Book
from src.books.serializers import BookSerializer


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter
