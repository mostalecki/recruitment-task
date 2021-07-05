from django.urls import path

from src.books.views import (
    BookCreateView,
    BookUpdateView,
    BookListView,
    BookDeleteView,
    BookImportView,
)

app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("create/", BookCreateView.as_view(), name="book-create"),
    path("import/", BookImportView.as_view(), name="book-import"),
    path("<pk>/update", BookUpdateView.as_view(), name="book-update"),
    path("<pk>/delete", BookDeleteView.as_view(), name="book-delete"),
]
