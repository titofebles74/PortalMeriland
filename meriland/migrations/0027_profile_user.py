# Generated by Django 3.0.5 on 2021-03-16 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meriland', '0026_profile_experiencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='experiencia',
            field=models.BooleanField(null=True),
        ),
    ]
