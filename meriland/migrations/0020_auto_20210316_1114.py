# Generated by Django 3.0.5 on 2021-03-16 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meriland', '0019_auto_20210315_1410'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-nacimiento']},
        ),
        migrations.AddField(
            model_name='profile',
            name='titulo',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='paramovil',
            field=models.BooleanField(default=True),
        ),
    ]
