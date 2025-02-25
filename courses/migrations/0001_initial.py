# Generated by Django 5.1.6 on 2025-02-24 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('credit_hours', models.IntegerField()),
                ('prerequisites', models.CharField(max_length=200)),
                ('level', models.CharField(choices=[('Undergraduate', 'UG'), ('Graduate', 'G'), ('Doctorate', 'PhD')], default='Undergraduate', max_length=13)),
                ('department', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='course_images/default-course.png', help_text='Upload a course image or leave blank to use default', upload_to='course_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Handout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='handouts/')),
                ('order', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handouts', to='courses.course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='LabWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='lab_work/')),
                ('order', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lab_work', to='courses.course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='lectures/')),
                ('order', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='courses.course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='VideoLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file_url', models.URLField(blank=True, max_length=500, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('duration', models.CharField(blank=True, max_length=50)),
                ('platform', models.CharField(choices=[('YT', 'YouTube'), ('VM', 'Vimeo'), ('FILE', 'Uploaded File'), ('OTHER', 'Other')], max_length=10)),
                ('order', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_lectures', to='courses.course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='CourseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('semester', models.CharField(choices=[('FALL', 'Fall'), ('SPRING', 'Spring'), ('SUMMER', 'Summer')], max_length=6)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='courses.course')),
            ],
            options={
                'ordering': ['-year', '-semester'],
                'unique_together': {('course', 'year', 'semester')},
            },
        ),
    ]
