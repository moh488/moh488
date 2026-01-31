
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from django.contrib import messages


# Create your views here.
def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        joining_date = request.POST.get('joining_date')
        student_phone = request.POST.get('student_phone')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')
    


        #retrieve dara from parent

        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_phone = request.POST.get('father_phone')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_phone = request.POST.get('mother_phone')
        mother_occupation = request.POST.get('mother_occupation')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')


        #save parent information

        parent = Parent.objects.create(
            father_name = father_name,
            father_occupation = father_occupation,
            father_phone = father_phone,
            father_email = father_email,
            mother_name = mother_name,
            mother_phone = mother_phone,
            mother_occupation = mother_occupation,
            mother_email = mother_email,
            present_address = present_address,
            permanent_address = permanent_address,
        )


        # save student informtion




        student = Student.objects.create(
            first_name = first_name,
            last_name = last_name,
            student_id  = student_id,
            gender = gender,
            date_of_birth = date_of_birth,
            student_class = student_class,
            joining_date = joining_date,
            student_phone = student_phone,
            admission_number = admission_number,
            section = section,
            student_image = student_image,
            parent = parent
        )

        messages.success(request, "student added successfuly")
                                                                 



    return render(request, "student/add-student.html")

def student_list(request):
    student_list = Student.objects.select_related('parent').all()
    context = {
        'student_list' : student_list
    }

    return render(request, "student/students.html", context)



def edit_student(request, slug):
    student = get_object_or_404(Student, slug = slug)
    parent = student.parent if hasattr(student,'parent') else None
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        joining_date = request.POST.get('joining_date')
        student_phone = request.POST.get('student_phone')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')
    


        #retrieve dara from parent

        parent.father_name = request.POST.get('father_name')
        parent.father_occupation = request.POST.get('father_occupation')
        parent.father_phone = request.POST.get('father_phone')
        parent.father_email = request.POST.get('father_email')
        parent.mother_name = request.POST.get('mother_name')
        parent.mother_phone = request.POST.get('mother_phone')
        parent.mother_occupation = request.POST.get('mother_occupation')
        parent.mother_email = request.POST.get('mother_email')
        parent.present_address = request.POST.get('present_address')
        parent.permanent_address = request.POST.get('permanent_address')
        parent.save()


        
      
       # save student informtion





        student.first_name = first_name
        student.last_name = last_name
        student.student_id  = student_id
        student.gender = gender
        student.date_of_birth = date_of_birth
        student.student_class = student_class
        student.joining_date = joining_date
        student.student_phone = student_phone
        student.admission_number = admission_number
        student.section = section
        student.student_image = student_image
        student.parent = parent
        student.save()
      
        return redirect("student_list")
    return render(request, "student/edit-student.html", {'student':student , 'parent':parent})


def view_student(request, slug):
    student = get_object_or_404(Student, student_id = slug)
    context = {
        'student' : student
    }
    return render(request, "student/student-details.html", context)
        


def delete_student(request,slug):
    if request.method =="POST":
        student = get_object_or_404(Student,slug = slug)
        student_name = f"{student.first_name} {student.last_name}"
        student.delete()

        return redirect ('student_list')
    return HttpResponseForbidden()
                                                                 
    

