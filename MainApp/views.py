from django.shortcuts import render, HttpResponseRedirect
from django . contrib import auth
from django . http import Http404


def base(request):
	return render(request, 'base.html')


def home(request):
	return render(request, 'home.html')