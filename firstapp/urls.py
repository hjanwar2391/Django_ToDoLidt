from django.urls import path
from firstapp.views import home, add_task, show_tasks, edit_task, complete_task, delete_task, completed_tasks

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_task, name='add_task'),
    path('show/', show_tasks, name='show_tasks'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('completed/', completed_tasks, name='completed_tasks'),
]
