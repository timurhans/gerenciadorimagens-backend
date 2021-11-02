# Generated by Django 3.2.4 on 2021-06-23 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0002_alter_media_image'),
        ('tags', '0001_initial'),
        ('colors', '0002_alter_color_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorVariationForProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colors.color')),
                ('media', models.ManyToManyField(to='media.Media')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('collection', models.CharField(max_length=100)),
                ('subcategory', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('colors', models.ManyToManyField(through='products.ColorVariationForProducts', to='colors.Color')),
                ('media', models.ManyToManyField(to='media.Media')),
                ('tags', models.ManyToManyField(to='tags.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='colorvariationforproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
