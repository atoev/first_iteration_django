from django.shortcuts import render

from .models import Course, Teacher


def home(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'home.html', {'courses': courses, 'teachers': teachers})


def about(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'about.html', {'course': course})
