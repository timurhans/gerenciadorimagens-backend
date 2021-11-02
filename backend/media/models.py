from tags.models import Tag
from django.db import models
from properties.models import MediaType, MediaStyle

def upload_to(instance, filename):
    return f'{instance.media_type}/{filename}'

class Media(models.Model):
    class PublicMedia(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(is_private=False)

    image = models.ImageField(upload_to=upload_to, default='socialist_dog.jpg') #requires pillow (pip instal pillow)
    media_type = models.ForeignKey(MediaType, on_delete=models.SET_NULL, null=True)
    style = models.ForeignKey(MediaStyle, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(to=Tag, blank=True)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    public_objects = PublicMedia()

    def __str__(self):
        return f"media {self.pk} / {self.media_type} / {self.style}"

    class Meta:
        verbose_name = "Mídia"
        verbose_name_plural = "Mídias"

