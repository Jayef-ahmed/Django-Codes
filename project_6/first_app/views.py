from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
def home(request):
    student = Student.objects.all()
    return render(request, 'home.html', {'data' : student})

def delete_student(request, roll):
    stu = Student.objects.get(pk = roll).delete()
    return redirect("home_page")
