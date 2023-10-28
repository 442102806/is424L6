from django.urls import path 
from .  import views 

urlpatterns = [
   path('students', views.studentsP, name="stu"),
   path('courses', views.coursesP, name="cour"),
   path("<int:studentId>", views.student, name="student"),
   path('students/add', views.addStudent, name="addStudent"),
   path('courses/add', views.addcourse, name="addcourse"),   
]