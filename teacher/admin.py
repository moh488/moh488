from django.contrib import admin
from. models import Teacher
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_name' , 'teacher_phone' , 'teacher_id' , 'teacher_email' , 'gender' , 'teacher_class' , 'date_of_birth' , 'section' , 'teacher_qualifications' , 'teacher_experience','address')
    search_fields = ('teacher_name', 'teacher_id', 'teacher_subject')
    list_filter = ('teacher_phone', 'teacher_class')
    readonly_fields = ('teacher_image',)
