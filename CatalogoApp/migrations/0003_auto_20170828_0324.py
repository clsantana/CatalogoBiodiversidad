# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 03:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CatalogoApp', '0002_auto_20170820_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=500, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(null=True, upload_to='images/user')),
                ('pais_origen', models.CharField(max_length=60)),
                ('ciudad', models.CharField(max_length=60)),
                ('comentario_interes', models.CharField(max_length=1000)),
                ('auth_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='especie',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CatalogoApp.CategoriaEspecie'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='taxonomia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CatalogoApp.TaxonomiaEspecie'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='especie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CatalogoApp.Especie'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CatalogoApp.Usuario'),
        ),
    ]