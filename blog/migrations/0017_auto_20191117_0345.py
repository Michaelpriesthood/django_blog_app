# Generated by Django 2.0.13 on 2019-11-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_comment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
