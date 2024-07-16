from django.shortcuts import render
from django.http import HttpResponse
import datetime

now = datetime.now()
# Create your views here.
def index(request, name):
    return render(request, "index.html", {
        "name": name.capitalize(),
         "msg": "Successful !",
        "h": now.hour ,
        "m": now.minute ,
        "s" :now.second
    })

