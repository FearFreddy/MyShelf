from django.db import models
from datetime import datetime, timedelta
from .util import get_remaining_days_from_datetime

# Create your models here.

class Folder(models.Model):
    folder_name = models.CharField(max_length=50)
    def __str__(self):
        return self.folder_name

class Todo(models.Model):
    in_folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    todo_text = models.CharField(max_length=500)
    due_date = models.DateTimeField()
    def get_remaining_days(self):
        return get_remaining_days_from_datetime(self.due_date)
    def __str__(self):
        return self.todo_text