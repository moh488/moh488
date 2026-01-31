from django.db import models
from django.utils.text import slugify

# Create your models here.

class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_phone = models.CharField(max_length=100)
    father_email = models.EmailField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_phone = models.CharField(max_length=100)
    mother_email = models.EmailField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField(null=True)

    def __str__(self)-> str:
        return f"{self.father_name} & {self.mother_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    student_phone = models.CharField(max_length=100)
    student_class = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=[('Male' , 'Male') , ('Female' , 'Female')])
    date_of_birth = models.DateField()
    joining_date = models.DateField()
    admission_number = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    student_image = models.ImageField(upload_to='student/')
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-({self.student_id})")
            super(Student,self).save(*args, **kwargs)
            


    
