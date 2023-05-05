import django_filters

from .models import Student
from .forms import choose_gender,STATE_CHOICES

class StudentFilters(django_filters.FilterSet):
    full_name=django_filters.CharFilter(lookup_expr='icontains')
    address=django_filters.CharFilter(lookup_expr='icontains')
    state=django_filters.ChoiceFilter(choices=STATE_CHOICES)
    class Meta:   
        model=Student
        fields='__all__'
        exclude=['dob','gender','image']