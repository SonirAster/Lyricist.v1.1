from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet

from .models import *
from .serializers import *
from .service import GroupFilter


class MainPageViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,):
    queryset = Song.objects.filter(time_create__gte=datetime.now(tz=timezone.utc)-timedelta(days=20))
    serializer_class = SongSerializer


class GroupViewSet(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GroupFilter
    queryset = Group.objects.all()
    serializer_class = GroupSerializer




