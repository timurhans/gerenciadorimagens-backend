from django.contrib import admin
from .models import Book

class Book_admin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Book, Book_admin)