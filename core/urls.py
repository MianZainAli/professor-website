from django.urls import path
from .views import index, introduction, courses, course_detail, notice_board, updates, contact

urlpatterns = [
    path('', index, name='index'),
    path('introduction/', introduction, name='introduction'),
    path('courses/', courses, name='courses'),
    path('courses/<int:course_id>/', course_detail, name='course_detail'),
    path('notice-board/', notice_board, name='notice-board'),
    path('updates/', updates, name='updates'),
    path('contact/', contact, name='contact'),
]
