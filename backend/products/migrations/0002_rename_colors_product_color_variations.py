# Generated by Django 3.2.4 on 2021-07-31 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='colors',
            new_name='color_variations',
        ),
    ]
