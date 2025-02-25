from django.contrib import admin
from .models import ChineseResource, CarouselMoment, Notice, Update


@admin.register(ChineseResource)
class ChineseResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('title', 'description')

@admin.register(CarouselMoment)
class CarouselMomentAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'important')
    list_filter = ('important', 'date')
    search_fields = ('title', 'content')
    
    
@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)
    search_fields = ('title', 'content')
    
