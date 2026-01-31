from django.db import models


# Create your models here.

class Departments(models.Model):
    dep_id = models.CharField(max_length=100)
    dep_name = models.CharField(max_length=100)
    head_of_department = models.CharField(max_length=100)
    dep_start_date = models.DateField()
    no_of_students = models.CharField(max_length=100, null=True)

    def __str__ (self)-> str:
        return f"{self.dep_name}  & {self.dep_id}"
    
    def save(self, *args, **kwargs):
        super(Departments, self) .save (*args, **kwargs)


    