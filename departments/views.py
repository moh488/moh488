from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from.models import *

# Create your views here.

def add_department(request):
    if request.method == 'POST':
        dep_id = request.POST.get("dep_id")
        dep_name = request.POST.get("dep_name")
        head_of_department = request.POST.get("head_of_department")
        dep_start_date =request.POST.get("dep_start_date")
        no_of_students = request.POST.get("no_of_students")

        #save departments information

        department = Departments.objects.create(
            dep_id = dep_id,
            dep_name = dep_name,
            head_of_department = head_of_department,
            dep_start_date = dep_start_date,
            no_of_students = no_of_students
        )
        messages.success(request, "department added succesfuly")
        
    
    return render(request , "departments/add-department.html")


def list_department(request):
    list_department = Departments.objects.all()
    context={
        'list_department' : list_department
    }
    return render(request, "departments/departments.html" , context)


def edit_department(request):
     department = get_object_or_404(Departments)
     if request.method == 'POST':
        dep_id = request.POST.get("dep_id")
        dep_name = request.POST.get("dep_name")
        head_of_department = request.POST.get("head_of_department")
        dep_start_date =request.POST.get("dep_start_date")
        no_of_students = request.POST.get("no_of_students")

        #save departments information

        
        department.dep_id = dep_id,
        department.dep_name = dep_name,
        department.head_of_department = head_of_department,
        department.dep_start_date = dep_start_date,
        department.no_of_students = no_of_students
        department.save()
        return redirect("list_department")
        

     return render(request, "departments/edit-department.html")

def delete_department(request):
    if request.method =="POST":
        department = get_object_or_404(Departments)
        dep_name = f"{department.dep_name} {department.dep_id}"
        department.delete()

        return redirect ('list_department')
    return HttpResponseForbidden()