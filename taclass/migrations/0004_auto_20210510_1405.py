# Generated by Django 3.2 on 2021-05-10 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taclass', '0003_alter_taclass_classimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taclass',
            name='assignment',
        ),
        migrations.RemoveField(
            model_name='taclass',
            name='assignmentTitle',
        ),
        migrations.RemoveField(
            model_name='taclass',
            name='listAssignment',
        ),
        migrations.RemoveField(
            model_name='taclass',
            name='receivedAssignment',
        ),
        migrations.AlterField(
            model_name='taclass',
            name='classImage',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='taclass',
            name='classLink',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
