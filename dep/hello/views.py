from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, name):
    if name ==" ":
        return HttpResponse("Hello world")
    else:
        return HttpResponse("Hello "+ name)

