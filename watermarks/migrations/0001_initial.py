# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-06 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatermarkImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('position_x', models.CharField(default=b'center', max_length=255, verbose_name='Position X')),
                ('position_y', models.CharField(default=b'center', max_length=255, verbose_name='Position Y')),
                ('opacity', models.FloatField(default=1, verbose_name='Opacity')),
                ('repeat', models.BooleanField(default=False, verbose_name='Repeat')),
                ('scale', models.BooleanField(default=False, verbose_name='Scale')),
                ('image', models.ImageField(upload_to=b'watermarks', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Watermark image',
                'verbose_name_plural': 'Watermark images',
            },
        ),
        migrations.CreateModel(
            name='WatermarkText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('position_x', models.CharField(default=b'center', max_length=255, verbose_name='Position X')),
                ('position_y', models.CharField(default=b'center', max_length=255, verbose_name='Position Y')),
                ('opacity', models.FloatField(default=1, verbose_name='Opacity')),
                ('repeat', models.BooleanField(default=False, verbose_name='Repeat')),
                ('scale', models.BooleanField(default=False, verbose_name='Scale')),
                ('text', models.CharField(max_length=255, verbose_name='Text')),
                ('font_file', models.FileField(blank=True, upload_to=b'watermarks', verbose_name='Font file')),
                ('font_size', models.IntegerField(default=16, verbose_name='Font size')),
                ('font_color', models.CharField(default=b'black', max_length=10, verbose_name='Font color')),
            ],
            options={
                'verbose_name': 'Watermark text',
                'verbose_name_plural': 'Watermark texts',
            },
        ),
    ]