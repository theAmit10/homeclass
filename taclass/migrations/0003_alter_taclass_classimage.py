# Generated by Django 3.2 on 2021-05-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taclass', '0002_auto_20210504_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taclass',
            name='classImage',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
