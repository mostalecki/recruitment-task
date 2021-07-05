from django.urls import path, include

urlpatterns = [
    path("books/", include("src.books.api_urls")),
]
