# Generated by Django 3.0.5 on 2021-03-18 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meriland', '0031_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('titulo', models.CharField(default='Sr(a)', max_length=50)),
                ('foto', models.ImageField(upload_to='img')),
                ('nacimiento', models.DateField(blank=True, null=True)),
                ('biografia', models.TextField()),
            ],
            options={
                'ordering': ['-nombre'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('resumen', models.TextField()),
                ('contenido', models.TextField()),
                ('esnoticia', models.BooleanField(default=True)),
                ('espromocion', models.BooleanField(default=False)),
                ('publicado', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now=True)),
                ('referencia', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='img')),
                ('clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clasificacion', to='meriland.Clasificacion')),
            ],
            options={
                'ordering': ['-creado'],
            },
        ),
    ]