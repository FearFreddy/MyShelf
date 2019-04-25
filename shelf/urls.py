from django.urls import path

from . import views

app_name = 'shelf'
urlpatterns = [
    # ex: /shelf/
    path('', views.index, name='index'),
    # ex: /folders/5/
    path('<int:folder_id>/', views.folder_detail, name='folder_detail'),
    path('<int:folder_id>/create_todo/', views.create_todo, name='create_todo'),
    path('delete_todo/', views.delete_todo, name='delete_todo'),
    path('create_folder/', views.create_folder, name='create_folder'),
    path('delete_folder/', views.delete_folder, name='delete_folder'),
]