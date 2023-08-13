from django.contrib import admin
from firstapp.models import  TaskModel
# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('taskTitle', 'taskDescription', 'is_completed')

admin.site.register(TaskModel, ToDoAdmin)