# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

my_choice = (
    ('c', 'calendar'),
    ('e', 'employee')
)
# Create your models here.


class AppSchedulerOption (models.Model):
    foreign_id = models.IntegerField(default=1, blank=True)
    key = models.CharField(max_length=255, primary_key=True)
    tab = models.IntegerField()
    value = models.CharField(max_length=255,blank=True, default='')
    label = models.CharField(max_length=255)
    type = models.CharField(max_length=32)
    order = models.IntegerField()
    visible = models.BooleanField()
    style = models.CharField(max_length=255,blank=True, default='')
    title = models.CharField(max_length=255,blank=True, default='Soon Coming...')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # (`key`, `tab_id`, `value`, `label`, `type`, `order`, `visible`, `style`)

    @classmethod
    def get_value(cls, key):

        """Get the value of a value via key.
        If not found, create one with the default value in
        settings.OPTIONS."""
        try:
            return cls.objects.get(key=key).value
        except:
            option = [x for x in settings.OPTIONS if x[0] == key][0]
            return option[2]

    @classmethod
    def get_label(cls, key):
        try:
            return cls.objects.get(key=key).label
        except:
            option = [x for x in settings.OPTIONS if x[0] == key][0]
            return option[3]

    @classmethod
    def get_all(cls, tab):

        options = cls.objects.all().filter(tab=tab).order_by('order')

        if options:
            return options
        else:
            options = [x for x in settings.OPTIONS if x[1] == tab]
            for option in options:
                cls.objects.create(key=option[0], tab=int(option[1]), value=option[2], label=option[3], type=option[4], order=int(option[5]), visible=bool(1), style=option[7], title=option[8])
            print(options)
            return cls.objects.all().filter(tab=tab).order_by('order')


class AppSchedulerWorkingDate (models.Model):
    foreign_id = models.IntegerField(default=1, blank=True)
    type = models.CharField(max_length=1, choices=my_choice, default='c')
    date = models.DateField(default='30-03-2017',blank=True)
    start_time = models.TimeField(default='09:30:00',blank=True)
    end_time = models.TimeField(default='09:30:00',blank=True)
    start_lunch = models.TimeField(default='09:30:00',blank=True)
    end_lunch = models.TimeField(default='09:30:00',blank=True)
    is_day_off = models.BooleanField(default=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)


class AppSchedulerWorkingTimes (models.Model):
    foreign_id = models.IntegerField(default=1, blank=True)
    type = models.CharField(max_length=1, choices=my_choice, default='c')
    monday_from = models.TimeField(default='09:30:00', blank=True)
    monday_to = models.TimeField(default='18:30:00', blank=True)
    monday_lunch_from = models.TimeField(default='12:30:00', blank=True)
    monday_lunch_to = models.TimeField(default='13:30:00', blank=True)
    monday_day_off = models.BooleanField(default=False, blank=True)
    tuesday_from = models.TimeField(default='09:30:00',blank=True)
    tuesday_to = models.TimeField(default='18:30:00',blank=True)
    tuesday_lunch_from = models.TimeField(default='12:30:00',blank=True)
    tuesday_lunch_to = models.TimeField(default='13:30:00',blank=True)
    tuesday_day_off = models.BooleanField(default=False,blank=True)
    wednesday_from = models.TimeField(default='09:30:00',blank=True)
    wednesday_to = models.TimeField(default='18:30:00',blank=True)
    wednesday_lunch_from = models.TimeField(default='12:30:00',blank=True)
    wednesday_lunch_to = models.TimeField(default='13:30:00',blank=True)
    wednesday_day_off = models.BooleanField(default=False,blank=True)
    thursday_from = models.TimeField(default='09:30:00',blank=True)
    thursday_to = models.TimeField(default='18:30:00',blank=True)
    thursday_lunch_from = models.TimeField(default='12:30:00',blank=True)
    thursday_lunch_to = models.TimeField(default='13:30:00',blank=True)
    thursday_day_off = models.BooleanField(default=False,blank=True)
    friday_from = models.TimeField(default='09:30:00',blank=True)
    friday_to = models.TimeField(default='18:30:00',blank=True)
    friday_lunch_from = models.TimeField(default='12:30:00',blank=True)
    friday_lunch_to = models.TimeField(default='13:30:00',blank=True)
    friday_day_off = models.BooleanField(default=False,blank=True)
    saturday_from = models.TimeField(default='09:30:00',blank=True)
    saturday_to = models.TimeField(default='18:30:00',blank=True)
    saturday_lunch_from = models.TimeField(default='12:30:00',blank=True)
    saturday_lunch_to = models.TimeField(default='13:30:00',blank=True)
    saturday_day_off = models.BooleanField(default=False,blank=True)
    sunday_from = models.TimeField(default='09:30:00',blank=True)
    sunday_to = models.TimeField(default='18:30:00',blank=True)
    sunday_lunch_from = models.TimeField(default='12:30:00',blank=True)
    sunday_lunch_to = models.TimeField(default='13:30:00',blank=True)
    sunday_day_off = models.BooleanField(default=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
