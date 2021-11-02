from django.db import models


class MediaType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"

class MediaStyle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Estilo"
        verbose_name_plural = "Estilos"

class ProductCollection(models.Model):
    name = models.CharField(max_length=100)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Coleção"
        verbose_name_plural = "Coleções"

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class ProductSubCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Sub-categoria"
        verbose_name_plural = "Sub-categorias"
    