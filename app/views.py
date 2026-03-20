from django.shortcuts import render, redirect
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            age=request.POST['age']
        )
        return redirect('/')
    return render(request, 'add.html')

def delete_student(request, id):
    Student.objects.get(id=id).delete()
    return redirect('/')