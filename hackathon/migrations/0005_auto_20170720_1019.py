# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0004_hackathon_background_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Height'),
        ),
        migrations.AddField(
            model_name='committee',
            name='width',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Width'),
        ),
        migrations.AlterField(
            model_name='committee',
            name='avatar',
            field=models.ImageField(height_field='height', upload_to='', verbose_name='Fotoğraf', width_field='width'),
        ),
    ]