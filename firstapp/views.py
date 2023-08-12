from django.shortcuts import render, redirect
from firstapp.forms import ToDoForm
from firstapp.models import ToDoModel
# Create your views here.

def home(request):
    return render(request, 'home.html')


def addToDo(request):
    if request.method == 'POST':
        form =  ToDoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.changed_data)
            return redirect('showToDo') 
             
    else:
        form = ToDoForm()
    return render(request, 'addToDo.html',{'form': form})

def showToDo(request):
    ToDo = ToDoModel.objects.all()
    print(ToDo)
    return render(request, 'showToDo.html', {'data': ToDo})

def editTodo(request, id):
    todo = ToDoModel.objects.get(pk = id)
    form = ToDoForm(instance=todo)
    if request.method == 'POST':
        todo =  ToDoForm(request.POST, instance = todo)
        if todo.is_valid():
            todo.save(commit=True)
            # print(book.changed_data)
            return redirect('showbook')
    else:
        form =  ToDoForm()
    return render(request, 'addToDo.html', {'form':form})   

def deleteTodo(request, id):
    todo = ToDoModel.objects.get(pk = id).delete()
    return redirect('showToDo')