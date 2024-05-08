from django.db import models

from apps.tags.models import Tag


class Post(models.Model):
    image = models.ImageField(
        upload_to='posts/'
    )
    text = models.TextField(
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    tag = models.ManyToManyField(
        Tag,
        related_name='posts_tag',
    )
    
    def __str__(self):
        return self.image.url
    

