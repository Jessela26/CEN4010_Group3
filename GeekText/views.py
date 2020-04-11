from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape

import Browse
from Browse.models import Book
from Browse.views import browse
from users.models import ShoppingCart, User

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
    books: [Book] = []
    saved: [Book] = []
    if request.user.is_authenticated:
        for book_id in request.user.shoppingcart.shopping_cart.split():
            books += Book.objects.filter(pk=book_id)
        for book_id in request.user.shoppingcart.save_for_later.split():
            saved += Book.objects.filter(pk=book_id)
    args['shopping_cart'] = books
    args['saved_books'] = saved
    return render(request, "shoppingcart.html", args)


def checkout(request):
    args = {}
    shopping_cart: [Book] = []
    cart_total: int = 0
    if request.user.is_authenticated:
        for book_id in request.user.shoppingcart.shopping_cart.split():
            shopping_cart += Book.objects.filter(pk=book_id)
    for book in shopping_cart:
        cart_total += book.price
    args['cart_size'] = len(shopping_cart)
    args['shopping_cart'] = shopping_cart
    args['total_price'] = cart_total
    return render(request, "checkout.html", args)


def browse(request):
    return Browse.views.browse(request)
