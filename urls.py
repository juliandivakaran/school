from django.urls import path
from calc.views import student_list

urlpatterns = [
    path('students/', student_list, name='student_list'),
]
