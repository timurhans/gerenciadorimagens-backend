from django.db import models

class Color(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=7)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Cor"
        verbose_name_plural = "Cores"

