from tkinter.ttk import Widget

from django.forms import DateInput
from django_filters import DateFilter, FilterSet, CharFilter

from .models import *

class RequestFilter(FilterSet):
    event_start_date = DateFilter(field_name='eventStartDate', lookup_expr='gte', label='Event Start Date')
    event_end_date = DateFilter(field_name='eventEndDate', lookup_expr='lte', label='Event End Date', widget=DateInput)

    class Meta:
        model = RequestList
        fields = '__all__'
        exclude = ['user', 'eventStartDate', 'eventEndDate']