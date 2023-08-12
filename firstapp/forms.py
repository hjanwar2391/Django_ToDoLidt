from django import forms
from firstapp.models import ToDoModel


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = ['id', 'name', 'description', 'status']
