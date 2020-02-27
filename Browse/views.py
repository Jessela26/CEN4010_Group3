from django.shortcuts import render
from django.core.paginator import Paginator
from Browse.models import Book


# Create your views here.
def browse(request):
    args = {}
    books = Book.objects.order_by('title')
    paginator = Paginator(books, 10)
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
    return render(request, "browse.html", args)
