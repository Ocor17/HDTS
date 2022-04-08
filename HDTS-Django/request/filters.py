from django_filters import DateFilter, FilterSet, CharFilter

from .models import *

class RequestFilter(FilterSet):
    event_start_date = DateFilter(field_name='eventStartDate', lookup_expr='gte', label='Event Start Date')
    event_end_date = DateFilter(field_name='eventEndDate', lookup_expr='lte', label='Event End Date')
    #event_start_date = CharFilter(field_name='Event Start Date')
    #event_end_date = CharFilter(field_name='Event End Date')


    class Meta:
        model = RequestList
        fields = '__all__'
        exclude = ['user', 'eventStartDate', 'eventEndDate']