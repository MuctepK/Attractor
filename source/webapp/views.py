from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task, STATUS_CHOICES
from .forms import TaskForm


def index_view(request, *args, **kwargs):
    tasks = Task.objects.all()
    return render(request, 'index.html',
                  {'tasks': tasks,
                   'status_choices': STATUS_CHOICES})


def task_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'create.html', context=
        {
            'form': form
        })
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'create.html', context ={'form': form})
        task = Task.objects.create(description=form.cleaned_data['description'],
                                   status=form.cleaned_data['status'],
                                   execution_date=form.cleaned_data['execution_date'],
                                   full_description=form.cleaned_data['full_description'])
        return redirect('task_view', pk=task.pk)


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')


def task_delete_selected_view(request):
    if request.method == 'GET':
        pks = request.GET.getlist('tasks')
        tasks = [get_object_or_404(Task, pk=pk) for pk in pks]
        return render(request, 'delete_selected.html', context={'tasks':tasks})
    elif request.method == 'POST':
        pks = request.POST.getlist('tasks')
        tasks = [get_object_or_404(Task, pk=pk) for pk in pks]
        for task in tasks:
            task.delete()
        return redirect('index')


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(data={'description':task.description,
                              'full_description':task.full_description,
                              'status':task.status,
                              'execution_date':task.execution_date})
        return render(request, 'update.html', context={ 'task':task,
                                                        'form': form,
                                                       'status_choices': STATUS_CHOICES})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.full_description = form.cleaned_data['full_description']
            task.status = form.cleaned_data['status']
            task.execution_date = form.cleaned_data['execution_date']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request,'update.html',context={
                'form':form,'task':task
            })


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', {'task': task,
                                         'status_choices': STATUS_CHOICES})
