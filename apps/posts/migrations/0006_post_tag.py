# Generated by Django 5.0.4 on 2024-05-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_tag'),
        ('tags', '0003_remove_tag_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='posts_tag', to='tags.tag'),
        ),
    ]
