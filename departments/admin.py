from django.contrib import admin
from.models import *



# Register your models here.

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('dep_name', 'dep_id', 'head_of_department', 'dep_start_date', 'no_of_students')
    search_fields = ('dep_name', 'dep_id')
