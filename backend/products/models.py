from sortedm2m.fields import SortedManyToManyField
from properties.models import ProductCategory, ProductCollection, ProductSubCategory
from django.db import models
from media.models import Media
from colors.models import Color


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(ProductSubCategory, on_delete=models.SET_NULL, null=True)
    collection = models.ForeignKey(ProductCollection, on_delete=models.SET_NULL, null=True)
    media = SortedManyToManyField(to=Media, blank=True)
    color_variations = models.ManyToManyField(to=Color, through='ColorVariationForProducts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

class ColorVariationForProducts(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    color = models.ForeignKey(to=Color, on_delete=models.CASCADE)
    media = SortedManyToManyField(to=Media, blank=True)

    def __str__(self):
        return f'{self.product.name} / {self.color.name}'

    class Meta:
        verbose_name = "Variação de cor"
        verbose_name_plural = "Variações de cor"