from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from books.models import CategoryBook, Book


class CategoryBooksListView(ListView):
    model = CategoryBook
    template_name = 'books/category_books_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'category_books'  # Default: object_list
    paginate_by = 8
    queryset = CategoryBook.published.all()  # Default: Model.objects.all()


class BooksListView(ListView):
    model = Book
    template_name = 'books/books_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'books'  # Default: object_list
    paginate_by = 8

    def get_queryset(self):
        obj = get_object_or_404(CategoryBook,
                                id=self.kwargs['pk'],
                                slug=self.kwargs['book'],
                                active=True)
        return obj.books.all()

    # queryset = category_book.books.all()  # Default: Model.objects.all()


def books_detail(request, book, pk):
    category_book = get_object_or_404(CategoryBook,
                                      id=pk,
                                      slug=book,
                                      active=True)

    books = category_book.books.all()

    context = {
        'books': books
    }
    return render(request, 'books/books_list.html', context)


def book_single(request, category, book, pk):
    book = get_object_or_404(Book,
                             id=pk,
                             slug=book,
                             active=True)

    return render(request, 'books/book_single.html', {'book': book})
