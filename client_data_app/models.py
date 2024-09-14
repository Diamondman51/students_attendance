from pyexpat import model
from _testmultiphase import Str
from django.db import models

# Create your models here.


class Parents(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=500)
    

class Subject(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    grade = models.IntegerField(choices=[(i, i) for i in range(1,12)])
    teacher = models.ManyToManyField('Curator', blank=True)


class Curator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=100)
    specialization = models.ForeignKey(Subject, on_delete=models.CASCADE)
    groups = models.ForeignKey('StudentGroup', on_delete=models.CASCADE)


class StudentGroup(models.Model):
    letter = models.CharField(max_length=10)
    grade = models.IntegerField(choices=[(i, i) for i in range(1, 12)], default=0)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    group = models.ForeignKey(StudentGroup, null=False, on_delete=models.CASCADE)
    parents = models.ManyToManyField(Parents, blank=False)
    address = models.CharField(max_length=500)
    curator = models.ForeignKey(Curator, blank=True, null=True, on_delete=models.CASCADE)


class Exercise(models.Model):
    teacher = models.ForeignKey(Curator, null=False, on_delete=models.CASCADE)
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE) 
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exercise = models.TextField(blank=False)


class Homework(models.Model):
    exercise = models.ForeignKey(Exercise, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    till = models.DateField(auto_now_add=True)

