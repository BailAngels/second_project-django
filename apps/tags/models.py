from django.db import models

from apps.posts.models import Post

class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='тег',
    )
    post = models.ManyToManyField(
        Post,
        related_name='tags',
    )

    def __str__(self):
        return self.name
    

