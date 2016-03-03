from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django .http import HttpResponseRedirect
from django.core.context_processors import csrf

from django .http import HttpResponseRedirect
from django.core.context_processors import csrf
from .forms import *

def getSavedBooks(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def getBooksIssued(request):

    bks_issued = BooksIssued.objects.all()

    return render(request, 'bksissued.html', {'bks_issued': bks_issued})

def issueBook(request):
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/issued")
    else:
        form = IssueBookForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form
    return render_to_response('issuebk.html', args)

def saveBook(request):
    if request.method == 'POST':
        form = SaveBookForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            HttpResponseRedirect("/books")

    else:

        form = SaveBookForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('savebk.html', args)

def home(request):

    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})








