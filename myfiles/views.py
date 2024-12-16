from django.shortcuts import render
from . models import *
# Create your views here.

def home(malumot):
    students = Cars.objects.all()
    courses = Brands.objects.all()
    context = {
        "students":students,
        "courses":courses
    }
    return render(malumot,'index.html',context)

def posts_by_category(request, course_id):
    courses = Brands.objects.all()
    students = Cars.objects.filter(course_id=course_id)

    context = {
        "courses": courses,
        'students': students
    }
    return render(request, 'index.html', context)


def post_detail(request, student_id):
    students = Cars.objects.get(pk=student_id)


    context = {
        "students": students
    }
    return render(request, 'detail.html', context)