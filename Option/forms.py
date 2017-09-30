from django import forms
from Option.models import *
from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SchedulerDateForm(forms.ModelForm):
    class Meta:
        model = AppSchedulerWorkingDate
        fields = [
            'date',
            'start_time',
            'end_time',
            'start_lunch',
            'end_lunch',
            'is_day_off'
        ]


class SchedulerTimeForm(forms.ModelForm):
    class Meta:
        model = AppSchedulerWorkingTimes
        fields = [
            'monday_from',
            'monday_to',
            'monday_lunch_from',
            'monday_lunch_to',
            'monday_day_off',
            'tuesday_from',
            'tuesday_to',
            'tuesday_lunch_from',
            'tuesday_lunch_to',
            'tuesday_day_off',
            'wednesday_from',
            'wednesday_to',
            'wednesday_lunch_from',
            'wednesday_lunch_to',
            'wednesday_day_off',
            'thursday_from',
            'thursday_to',
            'thursday_lunch_from',
            'thursday_lunch_to',
            'thursday_day_off',
            'friday_from',
            'friday_to',
            'friday_lunch_from',
            'friday_lunch_to',
            'friday_day_off',
            'saturday_from',
            'saturday_to',
            'saturday_lunch_from',
            'saturday_lunch_to',
            'saturday_day_off',
            'sunday_from',
            'sunday_to',
            'sunday_lunch_from',
            'sunday_lunch_to',
            'sunday_day_off'
        ]


class OptionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value, default_value in settings.OPTIONS:  # settings.OPTIONS
            self.fields[key] = forms.CharField(max_length=128)
            self.fields[key].value = value
            # get_or_create => (<Option: Option object>, False)
            optionObj, _ = AppSchedulerOption.objects.get_or_create(
                key=key,
                defaults={'value': default_value})
            self.fields[key].initial = optionObj.value
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, POST):
        for key, _, _ in settings.OPTIONS:
            AppSchedulerOption.objects.filter(key=key).update(value=POST[key])
