from django.http import Http404
from django.shortcuts import get_object_or_404, render
from courses.models import Course

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
