from django_filters import rest_framework as filters

from .models import Group


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class GroupFilter(filters.FilterSet):
    genre = CharFilterInFilter(field_name='genre__genre', lookup_expr='in')
    year = filters.RangeFilter()
    language = CharFilterInFilter(field_name='language__lang', lookup_expr='in')
    character = CharFilterInFilter(field_name='character__char', lookup_expr='in')

    class Meta:
        model = Group
        fields = ['genre', 'year', 'language', 'character', ]
