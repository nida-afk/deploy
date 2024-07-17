from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django import forms

class TaskForm(forms.Form):
    task = forms.CharField(max_length=100)
    priority = forms.IntegerField(max_value=10 , min_value= 5,  )


choicess ={}

taskss = []

class ChoicesForm(forms.Form):
    choices = forms.ChoiceField(choices=[('task1', 'Task 1'), ('task2', 'Task 2'), ('task3', 'Task 3')])

    delete = forms.ChoiceField(choices=[('task1', 'Task 1'), ('task2', 'Task 2'), ('task3', 'Task 3')])
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
            taskss.append(task)
            task_form = TaskForm()
    else:
        task_form = TaskForm()
    return render(request, 'tasks.html', {'tasks': taskss, 'form': task_form})

def choose(request):
    if request.method == 'POST':

        choice_form = ChoicesForm(request.POST)
        if choice_form.is_valid():
            choice = choice_form.cleaned_data['choices']
            choicess[choice] = 1
            if 'delete' in request.POST:
                delete = choice_form.cleaned_data['delete']
                if delete in choicess:
                    del choicess[delete]

            choice_form = ChoicesForm()

    else:
        choice_form = ChoicesForm()
        return render(request, 'choices.html',{
                'choices': choicess,
                'form': choice_form,
                'error': 'Invalid choice'
            })



