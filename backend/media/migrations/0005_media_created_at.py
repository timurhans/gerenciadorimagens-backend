# Generated by Django 3.2.4 on 2021-09-08 16:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_alter_media_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
