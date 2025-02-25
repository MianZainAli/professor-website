from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from .models import CarouselMoment, ChineseResource, Notice, Update, Contact
from .forms import ContactForm
import json

def index(request):
    cResources = ChineseResource.objects.all()
    cMoments = CarouselMoment.objects.filter(active=True).order_by('order')
    notices = Notice.objects.all().order_by('-date')[:3]
    updates = Update.objects.all().order_by('-date')[:3]
    return render(request, 'index.html', {
        'carouselMoments': cMoments, 
        'chineseResources': cResources,
        'notices': notices,
        'updates': updates
    })

def introduction(request):
    return render(request, 'about.html')

def notice_board(request):
    notices = Notice.objects.all()
    return render(request, 'notices.html', {
        'notices': notices
    })

def updates_view(request):
    updates = Update.objects.all()
    return render(request, 'updates.html', {
        'updates': updates
    })

def contact(request):
    return render(request, 'contact.html')

@require_http_methods(["POST"])
@csrf_protect
def submit_contact(request):
    try:
        data = json.loads(request.body)
        form = ContactForm(data)
        
        if form.is_valid():
            contact = form.save(commit=False)
            contact.ip_address = request.META.get('REMOTE_ADDR')
            contact.save()
            
            return JsonResponse({
                'status': 'success',
                'message': 'Your message has been sent successfully!'
            })
        else:
            # Get the first error message
            error = next(iter(form.errors.values()))[0]
            return JsonResponse({
                'status': 'error',
                'message': str(error)
            }, status=400)
            
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid request format'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': 'An error occurred while sending your message.'
        }, status=400)
