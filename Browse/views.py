from django.core.paginator import Paginator
from django.db.models import Q
from django.http import QueryDict
from django.shortcuts import render
from django.urls import resolve

from Browse.models import Book


# Create your views here.
def browse(request):
    if request.method == 'POST':
        return search(request, request.POST)
    args = {}
    books = Book.objects.order_by('title')
    paginator = Paginator(books, 9)
    for book in books:
        if book.description.__contains__('.'):
            book.description = book.description.split('.', 1)[0] + '.'
        if book.description.__contains__('!'):
            book.description = book.description.split('!', 1)[0] + '!'
        if book.description.__contains__('?'):
            book.description = book.description.split('?', 1)[0] + '?'
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    args['books'] = page_obj
    args['url_name'] = 'title'
    return render(request, "browse.html", args)


def author(request):
    args = {}
    books = Book.objects.order_by('author')
    paginator = Paginator(books, 9)
    for book in books:
        if book.description.__contains__('.'):
            book.description = book.description.split('.', 1)[0] + '.'
        if book.description.__contains__('!'):
            book.description = book.description.split('!', 1)[0] + '!'
        if book.description.__contains__('?'):
            book.description = book.description.split('?', 1)[0] + '?'
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    args['books'] = page_obj
    args['url_name'] = resolve(request.path_info).url_name
    return render(request, "browse.html", args)


def p_date_old2new(request):
    args = {}
    books = Book.objects.order_by('year', 'date_published')
    paginator = Paginator(books, 9)
    for book in books:
        if book.description.__contains__('.'):
            book.description = book.description.split('.', 1)[0] + '.'
        if book.description.__contains__('!'):
            book.description = book.description.split('!', 1)[0] + '!'
        if book.description.__contains__('?'):
            book.description = book.description.split('?', 1)[0] + '?'
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    args['books'] = page_obj
    args['url_name'] = resolve(request.path_info).url_name
    return render(request, "browse.html", args)


def p_date_new2old(request):
    args = {}
    books = Book.objects.order_by('-year', '-date_published')
    paginator = Paginator(books, 9)
    for book in books:
        if book.description.__contains__('.'):
            book.description = book.description.split('.', 1)[0] + '.'
        if book.description.__contains__('!'):
            book.description = book.description.split('!', 1)[0] + '!'
        if book.description.__contains__('?'):
            book.description = book.description.split('?', 1)[0] + '?'
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    args['books'] = page_obj
    args['url_name'] = resolve(request.path_info).url_name
    return render(request, "browse.html", args)


def search(request, search_term):
    search_term = QueryDict.copy(search_term)
    search_term = search_term.get('search_term')
    args = {}
    books = Book.objects.order_by('title').filter(Q(title__contains=search_term) | Q(genre__contains=search_term))

    paginator = Paginator(books, 9)
    for book in books:
        if book.description.__contains__('.'):
            book.description = book.description.split('.', 1)[0] + '.'
        if book.description.__contains__('!'):
            book.description = book.description.split('!', 1)[0] + '!'
        if book.description.__contains__('?'):
            book.description = book.description.split('?', 1)[0] + '?'
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    args['books'] = page_obj
    args['url_name'] = resolve(request.path_info).url_name
    args['searchterm'] = search_term
    print(resolve(request.path_info).url_name)
    return render(request, "browse.html", args)

def browse18(request):
    if request.method == 'POST':
        return search(request, request.POST)
    args = {}
    books = Book.objects.order_by('title')
    paginator = Paginator(books, 18)
    for book in books:
        if book.description.__contains__('.'):
            book.description = book.description.split('.', 1)[0] + '.'
        if book.description.__contains__('!'):
            book.description = book.description.split('!', 1)[0] + '!'
        if book.description.__contains__('?'):
            book.description = book.description.split('?', 1)[0] + '?'
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    args['books'] = page_obj
    args['url_name'] = 'title'
    return render(request, "browse.html", args)