import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
	# note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Driver
		fields = '__all__'
		exclude = ['driver_name','mobile_no','mohalla_or_village','district','state','vehicle_registration_no','vehicle_brand','vehicle_model','insurance_validity','insurance_type','registration_year','km_driven']
    