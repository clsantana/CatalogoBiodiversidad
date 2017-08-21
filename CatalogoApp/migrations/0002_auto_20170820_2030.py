# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 01:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CatalogoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nombre_cientifico', models.CharField(max_length=60)),
                ('desc_corta', models.CharField(max_length=150)),
                ('desc_larga', models.CharField(max_length=500)),
                ('foto', models.ImageField(null=True, upload_to='images')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ref1', to='CatalogoApp.CategoriaEspecie')),
            ],
        ),
        migrations.CreateModel(
            name='TaxonomiaEspecie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='especie',
            name='taxonomia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ref1', to='CatalogoApp.TaxonomiaEspecie'),
        ),
    ]