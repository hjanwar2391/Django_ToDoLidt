from django.contrib import admin
from firstapp.models import ToDoModel
# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status')

admin.site.register(ToDoModel, ToDoAdmin)