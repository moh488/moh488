from django.forms import SlugField
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from.models import*
from django.contrib import messages

# Create your views here.
def add_teacher(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('teacher_name')
        teacher_phone = request.POST.get('teacher_phone')
        teacher_id = request.POST.get('teacher_id')
        teacher_email = request.POST.get('teacher_email')
        teacher_class = request.POST.get('teacher_class')
        teacher_image = request.FILES.get('teacher_image')
        teacher_subject = request.POST.get('teacher_subject')
        teacher_qualifications = request.POST.get('teacher_qualifications')
        teacher_experience = request.POST.get('teacher_experience')
        section = request.POST.get('section')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        joining_date = request.POST.get('joining_date')
        address = request.POST.get('address')


        # save teacher information

        teacher = Teacher.objects.create(
            teacher_name = teacher_name,
            teacher_phone = teacher_phone,
            teacher_id = teacher_id,
            teacher_email = teacher_email,
            teacher_class = teacher_class,
            teacher_image = teacher_image,
            teacher_subject = teacher_subject,
            teacher_qualifications = teacher_qualifications,
            teacher_experience = teacher_experience,
            section = section,
            gender = gender,
            date_of_birth = date_of_birth,
            joining_date = joining_date,
            address = address
        )
        
        messages.success(request, "teacher added successfuly")



    return render(request, "teacher/add-teacher.html")


def list_teacher(request):
    list_teacher = Teacher.objects.all()
    context = {
        'list_teacher' : list_teacher
    } 
    return render(request, "teacher/teachers.html", context)


def view_teacher(request, slug):
    teacher = Teacher.objects.get(slug = slug)
    context = {
        'teacher' : teacher
    }
    return render(request, "teacher/teacher-details.html", context)

def edit_teacher(request, slug):
     teacher = get_object_or_404(Teacher, slug = slug)
     if request.method == 'POST':
        teacher_name = request.POST.get('teacher_name')
        teacher_phone = request.POST.get('teacher_phone')
        teacher_id = request.POST.get('teacher_id')
        teacher_email = request.POST.get('teacher_email')
        teacher_class = request.POST.get('teacher_class')
        teacher_image = request.FILES.get('teacher_image')
        teacher_subject = request.POST.get('teacher_subject')
        teacher_qualifications = request.POST.get('teacher_qualifications')
        teacher_experience = request.POST.get('teacher_experience')
        section = request.POST.get('section')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        joining_date = request.POST.get('joining_date')
        address = request.POST.get('address')


        # save teacher information

        
        teacher.teacher_name = teacher_name,
        teacher.teacher_phone = teacher_phone,
        teacher.teacher_id = teacher_id,
        teacher.teacher_email = teacher_email,
        teacher.teacher_class = teacher_class,
        teacher.teacher_image = teacher_image,
        teacher.teacher_subject = teacher_subject,
        teacher.teacher_qualifications = teacher_qualifications,
        teacher.teacher_experience = teacher_experience,
        teacher.section = section,
        teacher.gender = gender,
        teacher.date_of_birth = date_of_birth,
        teacher.joining_date = joining_date,
        teacher.address = address
        teacher.save()
        
        return redirect("list_teacher")
        
     return render(request, "teacher/edit-teacher.html", {'teacher' : teacher})


def delete_teacher(request,slug):
    if request.method =="POST":
        teacher = get_object_or_404(Teacher,slug = slug)
        teacher_name = f"{teacher.teacher_name} {teacher.teacher_id}"
        teacher.delete()

        return redirect ('list_teacher')
    return HttpResponseForbidden()
