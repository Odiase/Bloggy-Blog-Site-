# Generated by Django 3.2.9 on 2022-05-19 20:38

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_remove_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='featured_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='jpeg', keep_meta=True, null=True, quality=100, size=[320, 280], upload_to='blog_images'),
        ),
    ]