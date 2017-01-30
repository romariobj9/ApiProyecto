# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(default=b'', max_length=150, blank=True)),
                ('ciudad', models.CharField(default=b'', max_length=100, blank=True)),
                ('latitud', models.FloatField(default=None, max_length=15, blank=True)),
                ('longitud', models.FloatField(default=None, max_length=15, blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(default=b'', max_length=150, blank=True)),
                ('ciudad', models.CharField(default=b'', max_length=100, blank=True)),
                ('latitud', models.FloatField(default=None, max_length=15, blank=True)),
                ('longitud', models.FloatField(default=None, max_length=15, blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(default=b'', max_length=150, blank=True)),
                ('ciudad', models.CharField(default=b'', max_length=100, blank=True)),
                ('latitud', models.FloatField(default=None, max_length=15, blank=True)),
                ('longitud', models.FloatField(default=None, max_length=15, blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(default=b'', max_length=150, blank=True)),
                ('ciudad', models.CharField(default=b'', max_length=100, blank=True)),
                ('latitud', models.FloatField(default=None, max_length=15, blank=True)),
                ('longitud', models.FloatField(default=None, max_length=15, blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(default=b'', max_length=150, blank=True)),
                ('ciudad', models.CharField(default=b'', max_length=100, blank=True)),
                ('latitud', models.FloatField(default=None, max_length=15, blank=True)),
                ('longitud', models.FloatField(default=None, max_length=15, blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
