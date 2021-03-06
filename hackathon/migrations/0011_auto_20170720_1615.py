# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0010_auto_20170720_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='committee_background_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Jüriler Arkaplan Resmi'),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='footer_background_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Footer Arkaplan Resmi'),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='sponsors_background_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Sponsorlar Arka Planı'),
        ),
    ]
