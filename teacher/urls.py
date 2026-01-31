from django.contrib import admin
from django.urls import path , include
from.  import views
urlpatterns = [
  path('add-teacher/', views.add_teacher, name="add_teacher"),
  path('list-teacher/', views.list_teacher, name="list_teacher"),
  path('teacher/<str:slug>/', views.view_teacher, name="view_teacher"),
  path('edit-teacher/<str:slug>/', views.edit_teacher, name="edit_teacher"),
  path('delete-teacher/<str:slug>/', views.delete_teacher, name="delete_teacher"),
  ]