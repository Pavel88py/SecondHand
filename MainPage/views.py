from django.shortcuts import render, HttpResponseRedirect
from django . contrib import auth
from django . http import Http404


def home(request):
    return render(request, 'home.html')