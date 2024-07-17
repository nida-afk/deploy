from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django import forms



# Create your views here.
def index(request):
    now = datetime.datetime.now()
    if request.method == 'POST':
        name = request.POST["name"]
    else:
        name = ""
    return render(request, "index.html", {
        "name": name.capitalize(),
        "msg": "Successful !",
        "h": now.hour ,
        "m": now.minute ,
        "s" :now.second,
        "i": now.day
    })

