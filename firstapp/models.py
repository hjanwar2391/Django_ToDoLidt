from django.db import models

# Create your models here.

class ToDoModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField( max_length=30)
    description = models.TextField()
    status = models.CharField(max_length=30,  default='incomplete')

