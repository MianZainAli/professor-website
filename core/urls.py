from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('introduction/', views.introduction, name='introduction'),
    path('notice-board/', views.notice_board, name='notice-board'),
    path('updates/', views.updates_view, name='updates'),
    path('contact/', views.contact, name='contact'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
]
