# Generated by Django 3.1.6 on 2021-02-18 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meriland', '0009_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='paramovil',
            field=models.BooleanField(default=True),
        ),
    ]
