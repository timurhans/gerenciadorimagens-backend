from django.contrib import admin
from .models import Tag

class Tag_admin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Tag, Tag_admin)