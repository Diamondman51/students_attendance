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


class Curator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=100)


class StudentGroup(models.Model):
    letter = models.CharField(max_length=10)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    grade = models.IntegerField(choices=[(i, i) for i in range(1, 12)], default=0)
    group = models.ForeignKey(StudentGroup, null=False)
    parents = models.ManyToManyField(Parents, null=True, blank=True, related_name="")
    address = models.CharField(max_length=500)
    curator = models.ForeignKey(Curator, blank=True, null=True)
