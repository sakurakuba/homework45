from django.shortcuts import render

# Create your views here.
from todo.models import Task


def index_view(request):
    tasks = Task.objects.order_by('-created_at')
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


##def tasks(request):

