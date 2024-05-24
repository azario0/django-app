from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'todo/add_task.html')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')
