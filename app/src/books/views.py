from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib import messages

from src.books.forms import BookForm
from src.books.models import Book


class BookListView(ListView):
    model = Book
    template_name = "books/book-list.html"


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
