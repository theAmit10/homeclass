# Generated by Django 3.2 on 2021-05-04 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classCode', models.CharField(max_length=100)),
                ('classImage', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('teacherName', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
                ('assignment', models.FileField(upload_to='')),
                ('receivedAssignment', models.BooleanField(blank=True, default=False)),
                ('assignmentTitle', models.CharField(blank=True, max_length=100)),
                ('listAssignment', models.TextField(blank=True)),
                ('classTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('classLink', models.CharField(max_length=500)),
            ],
        ),
    ]
