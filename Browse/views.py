from django.shortcuts import render
from Browse.models import Book


# Create your views here.
def browse(request):
    args = {}
    books = Book.objects.all()
    args['Books'] = books
    return render(request, "browse.html", args)
