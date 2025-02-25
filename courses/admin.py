from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from courses.models import Course, CourseHistory, Handout, LabWork, Lecture, VideoLecture

class LectureInline(admin.TabularInline):
    model = Lecture
    extra = 0
    fields = ('title', 'order')
    readonly_fields = ('title',)
    can_delete = True
    show_change_link = True
    max_num = 0

class HandoutInline(admin.TabularInline):
    model = Handout
    extra = 0
    fields = ('title', 'order')
    readonly_fields = ('title',)
    can_delete = True
    show_change_link = True
    max_num = 0

class VideoLectureInline(admin.TabularInline):
    model = VideoLecture
    extra = 0
    fields = ('title', 'order')
    readonly_fields = ('title',)
    can_delete = True
    show_change_link = True
    max_num = 0

class LabWorkInline(admin.TabularInline):
    model = LabWork
    extra = 0
    fields = ('title', 'order')
    readonly_fields = ('title',)
    can_delete = True
    show_change_link = True
    max_num = 0

class CourseHistoryInline(admin.TabularInline):
    model = CourseHistory
    extra = 1
    ordering = ['-year', '-semester']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'department', 'level', 'credit_hours', 'add_materials')
    list_filter = ('department', 'level')
    search_fields = ('title', 'subject', 'description')
    fieldsets = (
        ('Course Information', {
           'fields': ('title', 'subject', 'description', 'credit_hours', 'prerequisites', 'level', 'department', 'image')
        }),
    )
    inlines = [LectureInline, HandoutInline, VideoLectureInline, LabWorkInline, CourseHistoryInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['image'].initial = 'course_images/default-course.png'
        return form

    def save_model(self, request, obj, form, change):
        if not obj.image:
            obj.image = 'course_images/default-course.png'
        super().save_model(request, obj, form, change)

    def add_materials(self, obj):
        add_lecture = reverse('admin:courses_lecture_add') + f'?course={obj.id}'
        add_handout = reverse('admin:courses_handout_add') + f'?course={obj.id}'
        add_video = reverse('admin:courses_videolecture_add') + f'?course={obj.id}'
        add_lab = reverse('admin:courses_labwork_add') + f'?course={obj.id}'
        
        return format_html(
            '<a class="addlink" href="{}">Add Lecture</a> | '
            '<a class="addlink" href="{}">Add Handout</a> | '
            '<a class="addlink" href="{}">Add Video</a> | '
            '<a class="addlink" href="{}">Add Lab</a>',
            add_lecture, add_handout, add_video, add_lab
        )
    add_materials.short_description = 'Add Materials'

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    ordering = ['order']

@admin.register(Handout)
class HandoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    ordering = ['order']

@admin.register(VideoLecture)
class VideoLectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    ordering = ['order']

@admin.register(LabWork)
class LabWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    ordering = ['order']


