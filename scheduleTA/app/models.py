from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=1, blank=False)
    username = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, unique=True)
    credit = models.IntegerField(blank=False)


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(User, on_delete=models.CaSCADE)
    name = models.CharField(max_length=100, blank=False)
    room_number = models.IntegerField(blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
