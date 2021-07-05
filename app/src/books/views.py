from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from src.books.filters import BookFilter
from src.books.forms import BookForm, BookSearchForm
from src.books.models import Book
from src.books.services import fetch_from_google_books, books_bulk_create_from_dict


class BookListView(View):
    def get(self, *args, **kwargs):
        f = BookFilter(self.request.GET, queryset=Book.objects.all())
        return render(self.request, "books/book-list.html", {"filter": f})


class BookCreateView(CreateView):
    template_name = "books/book-create.html"
    form_class = BookForm

    def get_success_url(self):
        instance: Book = self.object
        messages.add_message(
            self.request, messages.SUCCESS, f"Successfully added {instance.title}"
        )
        return reverse_lazy("books:book-list")


class BookUpdateView(UpdateView):
    model = Book
    template_name = "books/book-update.html"
    form_class = BookForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, f"Updated successfully")
        return reverse("books:book-update", args=(self.kwargs["pk"],))


class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/book-confirm-delete.html"

    def get_success_url(self):
        instance: Book = self.object
        messages.add_message(
            self.request, messages.SUCCESS, f"Successfully deleted {instance.title}"
        )
        return reverse_lazy("books:book-list")


class BookImportView(View):
    def get(self, *args, **kwargs):

        form = BookSearchForm(self.request.GET)
        books = []
        if form.is_valid() and self.request.GET.get("searchButton") == "submitted":
            books_dict = fetch_from_google_books(query=self.request.GET.get("query"),)

            self.request.session["imported_books_context"] = {"books": books_dict}

            books = books_bulk_create_from_dict(books_dict)

        return render(
            self.request, "books/book-import.html", {"form": form, "books": books}
        )

    def post(self, *args, **kwargs):
        volume_ids = self.request.POST["volume_ids"]
        books_to_add = [
            book
            for book in self.request.session["imported_books_context"]["books"]
            if book["volume_id"] in volume_ids
        ]
        books = books_bulk_create_from_dict(books_to_add)

        Book.objects.bulk_create(books)

        messages.add_message(
            self.request, messages.SUCCESS, f"Successfully added {len(books)} books"
        )
        return redirect("books:book-list")
