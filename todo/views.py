from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from todo.models import Task, STATUS_CHOICES


def index_view(request):
    tasks = Task.objects.order_by('-created_at')
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def add_task(request):
    if request.method == 'GET':
        return render(request, 'add.html', {'statuses': STATUS_CHOICES})
    else:
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        Task.objects.create(title=title, description=description, status=status, deadline=deadline)
        return render(request, 'add.html')


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', {"task": task})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', {'task': task})
    else:
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.deadline = request.POST.get('deadline')
        task.save()
        return redirect('task_view', pk=task.pk)


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'task': task})
    else:
        task.delete()
        return redirect('main')
