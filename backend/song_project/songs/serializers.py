from rest_framework import serializers

from .models import *


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'name', 'language', 'year',
            'genre', 'image', 'slug',
            'time_create', 'time_update',
        )


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = (
            'title', 'year', 'album',
            'group', 'time_create', 'time_update',
            'slug',)