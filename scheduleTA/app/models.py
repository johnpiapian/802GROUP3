from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=1, blank=False)
    name = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)
    skills = models.TextField(blank=True)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, unique=True)
    credit = models.IntegerField(blank=False)


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_number = models.IntegerField(blank=False, unique=True)
    class_type = models.CharField(max_length=50, blank=False)
    room_number = models.IntegerField(blank=False)
    teacher_name = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateField(blank=False)
    end_time = models.DateField(blank=False)
