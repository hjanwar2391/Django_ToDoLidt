from django.urls import path
from firstapp.views import home, addToDo,showToDo, deleteTodo,editTodo

urlpatterns = [
    path('', home, name='home'),
    path('addtodo/', addToDo, name='addToDo'),
    path('showtodo/', showToDo, name='showToDo'),
    path('delete/<int:id>', deleteTodo, name="deleteTodo"),
    path('edit/<int:id>', editTodo, name="editTodo"),
]
