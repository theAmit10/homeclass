# Generated by Django 3.2 on 2021-05-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taclass', '0004_auto_20210510_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taclass',
            name='classCode',
        ),
        migrations.AddField(
            model_name='taclass',
            name='className',
            field=models.CharField(default=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True), max_length=100),
        ),
        migrations.AlterField(
            model_name='taclass',
            name='subject',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
