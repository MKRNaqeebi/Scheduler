# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppSchedulerOption',
            fields=[
                ('foreign_id', models.IntegerField(blank=True, default=1)),
                ('key', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('tab', models.IntegerField()),
                ('value', models.CharField(blank=True, default='', max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=32)),
                ('order', models.IntegerField()),
                ('visible', models.BooleanField()),
                ('style', models.CharField(blank=True, default='', max_length=255)),
                ('title', models.CharField(blank=True, default='Soon Coming...', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppSchedulerWorkingDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foreign_id', models.IntegerField(blank=True, default=1)),
                ('type', models.CharField(choices=[('c', 'calendar'), ('e', 'employee')], default='c', max_length=1)),
                ('date', models.DateField(blank=True, default='30-03-2017')),
                ('start_time', models.TimeField(blank=True, default='09:30:00')),
                ('end_time', models.TimeField(blank=True, default='09:30:00')),
                ('start_lunch', models.TimeField(blank=True, default='09:30:00')),
                ('end_lunch', models.TimeField(blank=True, default='09:30:00')),
                ('is_day_off', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppSchedulerWorkingTimes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foreign_id', models.IntegerField(blank=True, default=1)),
                ('type', models.CharField(choices=[('c', 'calendar'), ('e', 'employee')], default='c', max_length=1)),
                ('monday_from', models.TimeField(blank=True, default='09:30:00')),
                ('monday_to', models.TimeField(blank=True, default='18:30:00')),
                ('monday_lunch_from', models.TimeField(blank=True, default='12:30:00')),
                ('monday_lunch_to', models.TimeField(blank=True, default='13:30:00')),
                ('monday_day_off', models.BooleanField(default=False)),
                ('tuesday_from', models.TimeField(blank=True, default='09:30:00')),
                ('tuesday_to', models.TimeField(blank=True, default='18:30:00')),
                ('tuesday_lunch_from', models.TimeField(blank=True, default='12:30:00')),
                ('tuesday_lunch_to', models.TimeField(blank=True, default='13:30:00')),
                ('tuesday_day_off', models.BooleanField(default=False)),
                ('wednesday_from', models.TimeField(blank=True, default='09:30:00')),
                ('wednesday_to', models.TimeField(blank=True, default='18:30:00')),
                ('wednesday_lunch_from', models.TimeField(blank=True, default='12:30:00')),
                ('wednesday_lunch_to', models.TimeField(blank=True, default='13:30:00')),
                ('wednesday_day_off', models.BooleanField(default=False)),
                ('thursday_from', models.TimeField(blank=True, default='09:30:00')),
                ('thursday_to', models.TimeField(blank=True, default='18:30:00')),
                ('thursday_lunch_from', models.TimeField(blank=True, default='12:30:00')),
                ('thursday_lunch_to', models.TimeField(blank=True, default='13:30:00')),
                ('thursday_day_off', models.BooleanField(default=False)),
                ('friday_from', models.TimeField(blank=True, default='09:30:00')),
                ('friday_to', models.TimeField(blank=True, default='18:30:00')),
                ('friday_lunch_from', models.TimeField(blank=True, default='12:30:00')),
                ('friday_lunch_to', models.TimeField(blank=True, default='13:30:00')),
                ('friday_day_off', models.BooleanField(default=False)),
                ('saturday_from', models.TimeField(blank=True, default='09:30:00')),
                ('saturday_to', models.TimeField(blank=True, default='18:30:00')),
                ('saturday_lunch_from', models.TimeField(blank=True, default='12:30:00')),
                ('saturday_lunch_to', models.TimeField(blank=True, default='13:30:00')),
                ('saturday_day_off', models.BooleanField(default=False)),
                ('sunday_from', models.TimeField(blank=True, default='09:30:00')),
                ('sunday_to', models.TimeField(blank=True, default='18:30:00')),
                ('sunday_lunch_from', models.TimeField(blank=True, default='12:30:00')),
                ('sunday_lunch_to', models.TimeField(blank=True, default='13:30:00')),
                ('sunday_day_off', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]