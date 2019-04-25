from django.db import models

# Create your models here.

class Folder(models.Model):
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    folder_name = models.CharField(max_length=50)
    def __str__(self):
        return self.folder_name

class Todo(models.Model):
    todo = models.ForeignKey(Folder, on_delete=models.CASCADE)
    todo_text = models.CharField(max_length=50)
    is_urgent = models.BooleanField
    def __str__(self):
        return self.todo_text