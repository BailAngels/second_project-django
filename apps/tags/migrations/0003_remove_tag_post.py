# Generated by Django 5.0.4 on 2024-05-08 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_tag_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
    ]