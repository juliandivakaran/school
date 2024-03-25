from django.shortcuts import render
from calc.models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
