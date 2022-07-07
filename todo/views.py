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
    return render(request, 'task.html', context={
        'task': task
    })

