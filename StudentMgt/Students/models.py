from django.db import models


# Create your models here.
class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    parent_contacts = models.PositiveIntegerField()
    form = models.CharField(max_length=50)

    def __str__(self):
        return f'Student: {self.first_name} {self.middle_name} {self.last_name}'
