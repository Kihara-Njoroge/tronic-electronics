import django_filters
from django_filters import CharFilter, NumberFilter
from .models import *


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',
                      lookup_expr='icontains', label='what are you looking for?')

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['description', 'price', 'image', 'vendor','category']
