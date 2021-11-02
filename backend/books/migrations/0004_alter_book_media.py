# Generated by Django 3.2.4 on 2021-09-13 23:02

from django.db import migrations
import sortedm2m.fields
from sortedm2m.operations import AlterSortedManyToManyField


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0008_alter_media_options'),
        ('books', '0003_alter_book_description'),
    ]

    operations = [
        AlterSortedManyToManyField(
            model_name='book',
            name='media',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='media.Media'),
        ),
    ]