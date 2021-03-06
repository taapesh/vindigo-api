# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 04:49
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VindigoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=64, primary_key=True, serialize=False)),
                ('device_name', models.CharField(default='', max_length=40)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('vehicle_id', models.CharField(blank=True, max_length=255, null=True)),
                ('time_driven', models.BigIntegerField(default=0)),
                ('distance_driven', models.DecimalField(decimal_places=2, default=0.0, max_digits=11)),
                ('location_address', models.CharField(default='', max_length=255)),
                ('location_lat', models.FloatField(blank=True, null=True)),
                ('location_lng', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('trip_id', models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=64, primary_key=True, serialize=False)),
                ('status', models.CharField(default='in_progress', max_length=20)),
                ('time_start', models.DateTimeField(auto_now_add=True)),
                ('time_end', models.DateTimeField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=64)),
                ('vehicle_id', models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=64)),
                ('distance', models.DecimalField(decimal_places=2, default=0.0, max_digits=11)),
                ('duration', models.BigIntegerField(default=0)),
                ('current_speed', models.FloatField(default=0.0)),
                ('average_moving_speed', models.FloatField(default=0.0)),
                ('average_speed', models.FloatField(default=0.0)),
                ('max_speed', models.IntegerField(default=0)),
                ('hard_accel_count', models.IntegerField(default=0)),
                ('hard_brake_count', models.IntegerField(default=0)),
                ('stop_count', models.IntegerField(default=0)),
                ('start_address', models.CharField(default='', max_length=255)),
                ('end_address', models.CharField(default='', max_length=255)),
                ('start_lat', models.FloatField(blank=True, null=True)),
                ('start_lng', models.FloatField(blank=True, null=True)),
                ('stop_lat', models.FloatField(blank=True, null=True)),
                ('stop_lng', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=64, primary_key=True, serialize=False)),
                ('device_id', models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=64)),
                ('year', models.IntegerField(default=-1)),
                ('make', models.CharField(default='', max_length=50)),
                ('model', models.CharField(default='', max_length=100)),
                ('trim', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
