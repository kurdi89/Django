# Generated by Django 2.2.3 on 2019-07-25 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_link',
        ),
        migrations.AddField(
            model_name='product',
            name='image_1_link',
            field=models.CharField(blank=True, default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='product',
            name='image_2_link',
            field=models.CharField(blank=True, default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3_link',
            field=models.CharField(blank=True, default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='product',
            name='image_4_link',
            field=models.CharField(blank=True, default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail_link',
            field=models.CharField(blank=True, default=None, max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, help_text='This is main thumbnail', upload_to=''),
        ),
    ]