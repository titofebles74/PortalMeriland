# Generated by Django 3.1.6 on 2021-02-22 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meriland', '0013_auto_20210221_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='espromocion',
            field=models.BooleanField(default=False),
        ),
    ]