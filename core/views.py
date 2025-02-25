from django.shortcuts import render
from .models import CarouselMoment, ChineseResource, Notice, Update
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
