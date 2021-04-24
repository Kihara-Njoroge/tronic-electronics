import django_filters
from django_filters import CharFilter, NumberFilter
from .models import *


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',
                      lookup_expr='icontains', label='Product')
    price_gt = NumberFilter(
        field_name='price', lookup_expr='gt', label='Price Min')
    price_lt = NumberFilter(
        field_name='price', lookup_expr='lt', label='Price Max')

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['description', 'price', 'image', 'vendor']
