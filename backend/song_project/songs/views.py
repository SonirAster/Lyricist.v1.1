from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet

from .models import *
from .serializers import GroupSerializer
from .service import GroupFilter


class GroupViewSet(GenericViewSet,
                   mixins.ListModelMixin):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GroupFilter
    queryset = Group.objects.filter(time_create__gte=datetime.now(tz=timezone.utc)-timedelta(days=20))
    serializer_class = GroupSerializer




