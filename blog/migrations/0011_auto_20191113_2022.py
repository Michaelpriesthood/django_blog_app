# Generated by Django 2.0.13 on 2019-11-14 04:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20191112_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
