from django.urls import path

from src.books.api_views import BookListAPIView

app_name = "books-api"

urlpatterns = [
    path("", BookListAPIView.as_view(), name="book-list-api"),
]
