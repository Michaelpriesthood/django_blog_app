# Generated by Django 2.0.13 on 2019-11-18 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20191118_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/%B/%d/%Y'),
        ),
    ]