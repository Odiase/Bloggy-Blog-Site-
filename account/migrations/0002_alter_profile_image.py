# Generated by Django 3.2.9 on 2022-05-19 09:28

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='C:\\Users\\acer\\django_projects\\bloggy/media/profile_images/profile-avatar.svg', force_format='jpeg', keep_meta=True, null=True, quality=100, size=[320, 280], upload_to='profile_images'),
        ),
    ]
