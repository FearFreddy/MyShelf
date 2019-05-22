from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Folder, Todo
# Create your views here.

def index(request):
    folders = Folder.objects.all()
    return render(request, 'shelf/index.html', {'folders': folders})

def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    return render(request, 'shelf/folder_detail.html', {'folder': folder})

def create_todo(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    folder.todo_set.create(todo_text=request.POST.get('todo_text', ''), due_date=request.POST.get('due_date', ''))
    return HttpResponseRedirect(reverse('shelf:folder_detail', args=(folder.id,)))

def edit_todo(request):
    todo = get_object_or_404(Todo, pk=request.POST.get('todo_id', 0))
    new_date = request.POST.get('due_date', '')
    if(new_date != ''):
        todo.due_date = new_date
        todo.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_todo(request):
    todo = get_object_or_404(Todo, pk=request.POST.get('todo_id', 0))
    todo.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def create_folder(request):
    Folder.objects.create(folder_name=request.POST.get('folder_name', 'Standard'))
    return HttpResponseRedirect(reverse('shelf:index'))

def delete_folder(request):
    folder = get_object_or_404(Folder, pk=request.POST.get('folder_id', 0))
    folder.delete()
    return HttpResponseRedirect(reverse('shelf:index'))