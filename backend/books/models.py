from media.models import Media
from django.db import models
from sortedm2m.fields import SortedManyToManyField

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    media = SortedManyToManyField(to=Media, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
