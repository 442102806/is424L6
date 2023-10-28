from django.shortcuts import render, HttpResponseRedirect
from .models import Student, Course

def studentsP(request):
    return render(request, "students.html",{
        "students": Student.objects.all()
    })

def coursesP(request):
    return render(request, "courses.html",{
        "courses": Course.objects.all()
    })

def student(request, studentId):
    student = Student.objects.get(id = studentId)
    course = student.cours.all()
    notCourses = Course.objects.exclude(courseName = Course).all()
    return render(request, "student.html",{
    "student": student,
    "course":course,
    "notCourses": notCourses
    })

def addStudent(request):
    if request.method == 'POST':
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        age = request.POST.get('age')
        IDs = request.POST.get('IDs')
        student = Student.objects.create(fName=fName, lName=lName, age=age, IDs=IDs )
    return render(request, 'addStudents.html')

def addcourse(request):
    if request.method == 'POST':
        courseName = request.POST.get('courseName')
        course = Course.objects.create(courseName = courseName)
        
    return render(request, 'addCourses.html')        
