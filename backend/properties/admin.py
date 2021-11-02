from django.contrib import admin
from .models import MediaType, MediaStyle
from .models import ProductCategory, ProductSubCategory, ProductCollection

admin.site.register(MediaType)
admin.site.register(MediaStyle)
admin.site.register(ProductCollection)
admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)
