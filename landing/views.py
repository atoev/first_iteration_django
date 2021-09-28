from django.shortcuts import render, redirect

from .models import Course, Teacher
from .forms import ApplicationForm


def home(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'home.html', {'courses': courses, 'teachers': teachers})


def about(request, pk):
    course = Course.objects.get(pk=pk)
    form = ApplicationForm(request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        is_success = True
        form.save()
        form = ApplicationForm()
    return render(request, 'about.html', {'course': course, 'form': form, 'is_success': is_success})
