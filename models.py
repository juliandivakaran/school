from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
