from urllib.parse import parse_qs, urlparse
from django.db import models
from django.forms import ValidationError

# Create your models here.
class Course(models.Model):
    LEVEL_CHOICES = [
        ('Undergraduate', 'UG'),
        ('Graduate', 'G'),
        ('Doctorate', 'PhD'),
    ]
    
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    credit_hours = models.IntegerField()
    prerequisites = models.CharField(max_length=200)
    level = models.CharField(max_length=13, choices=LEVEL_CHOICES, default='Undergraduate')
    department = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='course_images/', 
        default='course_images/default-course.png',
        help_text='Upload a course image or leave blank to use default',
        blank=True
    )
    
    @property
    def default_image(self):
        return 'course_images/default-course.png'  # Make sure this file exists in your media folder
    
    def get_image_url(self):
        return self.image.url if self.image else None

    def save(self, *args, **kwargs):
        if not self.image:
            self.image = self.default_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lectures')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='lectures/')
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def get_material_url(self):
        return self.file.url

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Handout(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='handouts')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='handouts/')
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def get_material_url(self):
        return self.file.url

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class VideoLecture(models.Model):
    PLATFORM_CHOICES = [
        ('YT', 'YouTube'),
        ('VM', 'Vimeo'),
        ('FILE', 'Uploaded File'),
        ('OTHER', 'Other')
    ]
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='video_lectures')
    title = models.CharField(max_length=200)
    file_url = models.URLField(max_length=500, blank=True, null=True)
    file = models.FileField(upload_to='videos/', blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True)
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def clean(self):
        if not self.file and not self.file_url:
            raise ValidationError('Either a file or URL must be provided')
        if self.file and self.file_url:
            raise ValidationError('Please provide either a file or URL, not both')
        if self.file and self.platform not in ['FILE', 'OTHER']:
            raise ValidationError('Platform should be FILE when uploading a video file')

    def get_embed_url(self):
        if self.file:
            return self.file.url
        if not self.file_url:
            return ''
            
        if self.platform == 'YT':
            parsed_url = urlparse(self.file_url)
            if 'youtube.com' in parsed_url.netloc:
                v = parse_qs(parsed_url.query).get('v', [''])[0]
                return f"https://www.youtube.com/embed/{v}"
            elif 'youtu.be' in parsed_url.netloc:
                v = parsed_url.path.lstrip('/')
                return f"https://www.youtube.com/embed/{v}"
        
        elif self.platform == 'VM':
            parsed_url = urlparse(self.file_url)
            video_id = parsed_url.path.lstrip('/')
            return f"https://player.vimeo.com/video/{video_id}"
            
        return self.file_url

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class LabWork(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lab_work')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='lab_work/')
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def get_material_url(self):
        return self.file.url

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class CourseHistory(models.Model):
    SEMESTER_CHOICES = [
        ('FALL', 'Fall'),
        ('SPRING', 'Spring'),
        ('SUMMER', 'Summer'),
    ]
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='history')
    year = models.PositiveIntegerField()
    semester = models.CharField(max_length=6, choices=SEMESTER_CHOICES)

    class Meta:
        ordering = ['-year', '-semester']
        unique_together = ['course', 'year', 'semester']

    def __str__(self):
        return f"{self.course.title} - {self.semester} {self.year}"

    def get_formatted_semester(self):
        return f"{self.semester.capitalize()} {self.year}"

