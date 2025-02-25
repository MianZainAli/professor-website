from django.db import models
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.jpeg', '.png', '.mp4', '.mov']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Allowed extensions are: ' + ', '.join(valid_extensions))

def validate_file_size(value):
    filesize = value.size
    max_size = 50 * 1024 * 1024  # 50MB
    if filesize > max_size:
        raise ValidationError(f'Maximum file size is {filesizeformat(max_size)}')

class ChineseResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(
        upload_to='chinese_resources/',
        validators=[validate_file_extension, validate_file_size],
        help_text='Allowed file types: PDF, DOC, DOCX, JPG, JPEG, PNG, MP4, MOV. Max size: 50MB'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def get_file_url(self):
        return self.file.url if self.file else None
    
    def __str__(self):
        return self.title
    
    
class CarouselMoment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='carousel_moments/',
        help_text='Recommended size: 1920x1080px'
    )
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    important = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
    
class Update(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
