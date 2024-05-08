from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='тег',
    )

    def __str__(self):
        return self.name
    

