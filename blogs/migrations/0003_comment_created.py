# Generated by Django 3.2.9 on 2022-05-17 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20220518_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
