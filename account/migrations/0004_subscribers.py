# Generated by Django 3.2.9 on 2022-05-20 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed', models.ManyToManyField(related_name='subscribed', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='my_subscribers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
