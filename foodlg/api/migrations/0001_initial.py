# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-11 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DishNutrient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=10)),
                ('quantity', models.FloatField(default=0)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nutrients', to='foodlg_api.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('group', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='dishnutrient',
            name='nutrient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodlg_api.Nutrient'),
        ),
    ]
