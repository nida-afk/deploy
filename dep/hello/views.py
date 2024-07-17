from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django import forms

class TaskForm(forms.Form):
    task = forms.CharField(max_length=100)

taskss = []
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

def tasks(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.cleaned_data['task']
            taskss.append(task_form)
            task_form = TaskForm()
    else:
        task_form = TaskForm()
    taskss.append(task_form)
    return render(request, 'tasks.html', {'tasks': taskss, 'form': task_form})
