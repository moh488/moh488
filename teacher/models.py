from django.db import models
from django.utils.text import slugify

# Create your models here.
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    teacher_phone = models.CharField(max_length=100)
    teacher_email = models.EmailField(max_length=100)
    teacher_id = models.CharField(max_length=50)
    teacher_image = models.ImageField(upload_to='teacher/', null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100, choices=[('Male' , 'Male') , ('Female' , 'Female')])
    joining_date = models.DateField()
    teacher_qualifications = models.CharField(max_length=100)
    teacher_experience = models.CharField(max_length=100)
    teacher_class = models.CharField(max_length=100)
    teacher_subject = models.CharField(max_length = 40)
    section = models.CharField(max_length=60)
    address = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    # save teacher information
    
    def __str__ (self)-> str:
        return f"{self.teacher_name} & {self.teacher_id}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify (f"{self.teacher_name}-{self.teacher_phone}-({self.teacher_id})")
            super(Teacher,self).save(*args, **kwargs)