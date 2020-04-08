from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape

import Browse
from Browse.models import Book
from Browse.views import browse

def homepage(request):
    return render(request, "homepage.html")


def wishlists(request):
    title = request.GET.get('title')
    author = request.GET.get('author')

    if title and author:
        return HttpResponse(escape(repr(title + author)))

    return render(request, "wishlist.html")


def cart(request):
    args = {}
    books = Book.objects.all()
    for book in books:
        if book.description.__contains__('.'):
            book.description = book.description.split('.', 1)[0] + '.'
        if book.description.__contains__('!'):
            book.description = book.description.split('!', 1)[0] + '!'
        if book.description.__contains__('?'):
            book.description = book.description.split('?', 1)[0] + '?'
    args['books'] = books
    return render(request, "shoppingcart.html", args)


def checkout(request):
    return render(request, "checkout.html")


def browse(request):
    return Browse.views.browse(request)
