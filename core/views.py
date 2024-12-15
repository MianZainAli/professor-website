from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import Course

def index(request):
    return render(request, 'index.html')

def introduction(request):
    return render(request, 'about.html')

def courses(request):
    try:
        courses = Course.objects.all()
        if not courses.exists():
            return render(request, 'courses.html', {
                'courses': None,
                'message': 'No courses are currently available.'
            })
        return render(request, 'courses.html', {'courses': courses})
    except Exception as e:
        return render(request, 'courses.html', {
            'courses': None,
            'error': 'An error occurred while fetching courses.'
        })

def course_detail(request, course_id):
    try:
        course = get_object_or_404(Course, id=course_id)
        return render(request, 'course-details.html', {'course': course})
    except Http404:
        return render(request, 'course-details.html', {
            'error': 'The requested course does not exist.'
        })
    except Exception as e:
        return render(request, 'course-details.html', {
            'error': 'An error occurred while fetching the course details.'
        })

def notice_board(request):
    return render(request, 'notices.html')

def updates(request):
    return render(request, 'updates.html')

def contact(request):
    return render(request, 'contact.html')
