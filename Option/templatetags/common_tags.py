from django import template
from Option.models import *
register = template.Library()

from datetime import datetime


@register.simple_tag
def option(key):
    return 1
    #Option.get_value(key)


@register.simple_tag
def get_time(date):
    datetime.strptime(date, '%H:%m:%s').time()


@register.simple_tag
def value_by_index(arr,index):
    return arr[index]


@register.assignment_tag
def value_by_index_assign(arr,index):
    return arr[index]


@register.assignment_tag
def split_string_colon(value):
    return value.split('::')


@register.assignment_tag
def split_string(value):
    return value.split('|')


@register.assignment_tag
def zip_it(key):
    label = AppSchedulerOption.get_label(key).split('::')
    value = AppSchedulerOption.get_value(key).split('::')
    return zip(value[0].split('|'),label[0].split('|'))