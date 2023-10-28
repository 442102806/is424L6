from django.db import models

class Course(models.Model):
    courseName = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.courseName}"


class Student(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    age = models.IntegerField()
    IDs = models.IntegerField()
    cours = models.ManyToManyField(Course, blank = True, related_name="students")

    def __str__(self):
        return f"{self.IDs},{self.fName} {self.lName}, {self.age} old"





