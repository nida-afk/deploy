from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def index(request):
    name = request.POST["name"]
    now = datetime.datetime.now()
    return render(request, "index.html", {
        "name": name.capitalize(),
        "msg": "Successful !",
        "h": now.hour ,
        "m": now.minute ,
        "s" :now.second,
        "i": now.day
    })

