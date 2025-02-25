from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('introduction/', introduction, name='introduction'),
    path('notice-board/', notice_board, name='notice-board'),
    path('updates/', updates_view, name='updates'),
    path('contact/', contact, name='contact'),
]
