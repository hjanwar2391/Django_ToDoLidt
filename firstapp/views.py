from django.shortcuts import render, redirect
from firstapp.forms import TaskForm
from firstapp.models import TaskModel
# Create your views here.

def home(request):
    return render(request, 'home.html')


def add_task(request):
    if request.method == 'POST':
        form =  TaskForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.changed_data)
            return redirect('show_tasks') 
             
    else:
        form = TaskForm()
    return render(request, 'add_task.html',{'form': form})

def show_tasks(request):
    ToDo = TaskModel.objects.all()
    print(ToDo)
    return render(request, 'show_task.html', {'data': ToDo})

def edit_task(request, id):
    todos = TaskModel.objects.get(pk = id)
    form = TaskForm(instance = todos)
    if request.method == 'POST':
        todos =  TaskForm(request.POST, instance = todos)
        if todos.is_valid():
            todos.save(commit=True)
            # print(book.changed_data)
            return redirect('show_tasks')
    else:
        todos =  TaskForm()
    return render(request, 'show_task.html', {'form':form}) 

def complete_task(request, id):
    todo = TaskModel.objects.get( pk=id)
    todo.status = True
    todo.save()
    return redirect('completed_tasks')

def delete_task(request, id):
    todo = TaskModel.objects.get(pk = id).delete()
    return redirect('show_tasks')

def completed_tasks(request):
    completedToDo = TaskModel.objects.filter(status=True)
    return render(request, 'completed_tasks.html', {'completed': completedToDo})

