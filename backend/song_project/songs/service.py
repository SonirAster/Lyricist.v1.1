from django_filters import rest_framework as filters

from songs.models import Group


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class GroupFilter(filters.FilterSet):
    genre = CharFilterInFilter(field_name='genre__genre', lookup_expr='in')
    year = filters.RangeFilter()

    class Meta:
        model = Group
        fields = ['genre', 'year']