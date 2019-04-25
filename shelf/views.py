from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Folder, Todo
# Create your views here.

def index(request):
    root_folders = Folder.objects.filter(parent_folder__isnull=True)
    context = {'root_folders': root_folders}
    return render(request, 'shelf/index.html', context)

def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    subfolders = Folder.objects.filter(parent_folder=folder_id)
    return render(request, 'shelf/folder_detail.html', {'folder': folder, 'subfolders': subfolders})

def create_todo(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    folder.todo_set.create(todo_text=request.POST.get('todo_text', ''))
    return HttpResponseRedirect(reverse('shelf:folder_detail', args=(folder.id,)))

def delete_todo(request):
    todo = get_object_or_404(Todo, pk=request.POST.get('todo_id', 0))
    todo.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def create_folder(request):
    if('parent_folder' in request.POST):
        parent_folder_instance = get_object_or_404(Folder, pk=request.POST['parent_folder'])
        Folder.objects.create(folder_name=request.POST['folder_name'], parent_folder=parent_folder_instance)        
        return HttpResponseRedirect(reverse('shelf:folder_detail', args=(parent_folder_instance.id,)))
    else:
        Folder.objects.create(folder_name=request.POST.get('folder_name', 'Standard'))
        return HttpResponseRedirect(reverse('shelf:index'))

def delete_folder(request):
    folder = get_object_or_404(Folder, pk=request.POST.get('folder_id', 0))
    folder.delete()
    if(folder.parent_folder):
        return HttpResponseRedirect(reverse('shelf:folder_detail', args=(folder.parent_folder.id,)))
    else:
        return HttpResponseRedirect(reverse('shelf:index'))

        