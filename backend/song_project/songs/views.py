from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet

from .models import *
from .serializers import GroupSerializer


class GroupViewSet(GenericViewSet,
                   mixins.ListModelMixin):
    filter_backends = (DjangoFilterBackend,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer




