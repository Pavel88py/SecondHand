from django.shortcuts import render, HttpResponseRedirect
from django . contrib import auth
from django . http import Http404


def home(request):
    return render(request, 'home.html')


def uroom(request):
    return render(request, 'uroom.html')


def itemform(request):
    return render(request, 'itemform.html')
