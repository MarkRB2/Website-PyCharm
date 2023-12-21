from django.shortcuts import render, redirect
from .models import Task, Products
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')

    form = TaskForm()
    context = {
       'form': form
    }
    return render(request, 'main/create.html', context)


def tov(request):
    product = Products.objects.all()
    return render(request, 'main/tov.html', {'product': product})