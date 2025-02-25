from django.contrib import admin
from django.utils.html import format_html
from .models import ChineseResource, CarouselMoment, Notice, Update, Contact

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

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'ip_address', 'is_read', 'message_preview')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'ip_address')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 20

    def message_preview(self, obj):
        return format_html('<span title="{}">{}</span>', 
                         obj.message, 
                         obj.message[:50] + '...' if len(obj.message) > 50 else obj.message)
    message_preview.short_description = 'Message'

    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} messages marked as read.')
    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, f'{updated} messages marked as unread.')
    mark_as_unread.short_description = "Mark selected messages as unread"

    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email')
        }),
        ('Message Details', {
            'fields': ('subject', 'message')
        }),
        ('Status Information', {
            'fields': ('is_read', 'created_at', 'ip_address'),
            'classes': ('collapse',)
        }),
    )

