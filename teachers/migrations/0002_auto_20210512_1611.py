# Generated by Django 3.2 on 2021-05-12 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachers',
            old_name='firstName',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='teachers',
            old_name='lastName',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='teachers',
            old_name='userName',
            new_name='username',
        ),
    ]