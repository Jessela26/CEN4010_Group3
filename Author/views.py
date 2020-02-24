from django.shortcuts import render
from Browse.models import Book


def author(request, book_author):
    args = {}
    book = Book.objects.filter(author=book_author)
    args['books'] = book
    args['book_author'] = book_author
    return render(request, "Author.html", args)
