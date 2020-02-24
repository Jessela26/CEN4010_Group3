from django.shortcuts import render
from Browse.models import Book


def details(request, book_id):
    args = {}
    book = Book.objects.get(pk=book_id)
    args['book'] = book
    return render(request, "BookDetails.html", args)
