# Generated by Django 3.2.4 on 2021-08-10 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_colors_product_color_variations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='style',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
    ]