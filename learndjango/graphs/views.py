from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world")

def foobar(request):
    return HttpResponse("foobar")
