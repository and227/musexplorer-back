# Generated by Django 2.2.5 on 2021-01-20 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muzservice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='genre',
        ),
    ]
