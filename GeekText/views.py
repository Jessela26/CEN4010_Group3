from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape


def homepage(request):
    return render(request, "homepage.html")


def wishlist(request):
    title = request.GET.get('title')
    author = request.GET.get('author')

    if title and author:
        return HttpResponse(escape(repr(title + author)))

    return render(request, "wishlist.html")


def cart(request):
    return render(request, "shoppingcart.html")

def checkout(request):
    return render(request, "checkout.html")

def browse(request):
    return render(request, "browse.html")
