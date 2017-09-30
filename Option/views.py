# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, HttpResponseRedirect
from .forms import *
from django.views.generic.edit import FormView


# Create your views here.

def index(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            option = AppSchedulerOption.objects.filter(key=key)
            if option:
                option.update(value=value)
    template = loader.get_template('index.html')
    context = {
        'booking_payment': AppSchedulerOption.get_all('7'),
        'booking_option': AppSchedulerOption.get_all('3'),
        'working_time_default': AppSchedulerWorkingTimes.objects.last(),
        'working_time_custom': AppSchedulerWorkingDate.objects.all()
    }
    return HttpResponse(template.render(context, request))


def working_date_default(request):
    if request.method == 'POST':
        date = request.POST.get('date', '')
        start_time = request.POST.get('start_time', '')
        end_time = request.POST.get('end_time', '')
        start_lunch = request.POST.get('start_lunch', '')
        end_lunch = request.POST.get('end_lunch', '')
        is_day_off = request.POST.get('is_day_off', '')
        if is_day_off == '':
            is_day_off = '0'
        scheduler_date = AppSchedulerWorkingDate(date=date,start_time=start_time,end_time=end_time,start_lunch=start_lunch,end_lunch=end_lunch,is_day_off=is_day_off)
        scheduler_date.save()
    return HttpResponseRedirect('/')


def working_date_default_edit(request):
    if request.method == 'POST':
        my_id = request.POST.get('id', '')
        date = request.POST.get('date', '')
        start_time = request.POST.get('start_time', '')
        end_time = request.POST.get('end_time', '')
        start_lunch = request.POST.get('start_lunch', '')
        end_lunch = request.POST.get('end_lunch', '')
        is_day_off = request.POST.get('is_day_off', '')
        if is_day_off == '':
            is_day_off = '0'
        scheduler_date = AppSchedulerWorkingDate.objects.get(id=my_id)
        scheduler_date.date=date
        scheduler_date.start_time=start_time
        scheduler_date.end_time=end_time
        scheduler_date.start_lunch=start_lunch
        scheduler_date.end_lunch=end_lunch
        scheduler_date.is_day_off=is_day_off
        scheduler_date.save()
    return HttpResponseRedirect('/')


def working_time_default(request):
    if request.method == 'POST':
        form = SchedulerTimeForm(request.POST)
        scheduler_time = form.save(commit=False)
        scheduler_time.save()
    return HttpResponseRedirect('/')


def bookings_payments(request):
    if request.method == 'Post':
        for key, value in request.POST.items():
            option = AppSchedulerOption.objects.get(key=key)
            if option:
                option.set_value(value)
            else:
                option = AppSchedulerOption(key=key, value=value)
            option.save(force_insert=True)
        template = loader.get_template('index.html')
        context = {
            'options': AppSchedulerOption.objects.get()
        }
        return HttpResponse(template.render(context, request))
    else:
        redirect('/')


class OptionSettings(FormView):
    template_name = "index.html"
    form_class = OptionForm
    success_url = '.'  # whatever.

    def form_valid(self, form):
        super().form_valid(form)
        form.save(self.request.POST)  # pass POST dict to LabelForm.save()
        return HttpResponseRedirect(self.get_success_url())
