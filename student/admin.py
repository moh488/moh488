from django.contrib import admin
from. models import *

# Register your models here.
@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_phone',  'mother_phone')
    search_fields = ('father_name', 'mother_name', 'father_phone', 'mother_phone')
    list_filter = ('father_name', 'mother_name')



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'student_phone', 'student_class', 'gender', 'date_of_birth', 'joining_date', 'admission_number', 'section')
    search_fields = ('first_name', 'last_name', 'student_id', 'student_class', 'admission_number')
    list_filter = ('gender', 'student_class', 'section')
    readonly_fields = ('student_image',)