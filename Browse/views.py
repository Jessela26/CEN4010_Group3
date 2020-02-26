from django.shortcuts import render
from Browse.models import Book


# Create your views here.
def browse(request):
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
    return render(request, "browse.html", args)
