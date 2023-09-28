from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from .models import *
from .serializers import *
from .service import GroupFilter


class GroupViewSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 10000


class GroupViewSet(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,):
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = GroupFilter
    search_fields = ('name',)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = GroupViewSetPagination


class MainPageViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,):
    queryset = Song.objects.filter(time_create__gte=datetime.now(tz=timezone.utc)-timedelta(days=20), is_published=True)
    serializer_class = SongSerializer








