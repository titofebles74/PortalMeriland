# Generated by Django 3.1.6 on 2021-02-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meriland', '0002_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='atendido',
            field=models.BooleanField(default=False),
        ),
    ]