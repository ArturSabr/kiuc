# Generated by Django 4.2 on 2023-04-24 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='image',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image',
        ),
    ]
