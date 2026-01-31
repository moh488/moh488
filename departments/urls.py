from django.contrib import admin
from django.urls import path , include
from.import views


urlpatterns = [

   path('add/', views.add_department, name="add_departments"),
   path('list/', views.list_department, name="list_department"),
   path('edit/', views.edit_department, name="edit_department"),
   path('delete/', views.delete_department, name="delete_department")
]