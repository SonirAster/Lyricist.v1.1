from rest_framework import serializers

from .models import *


class GroupSerializer(serializers.ModelSerializer):
    language = serializers.SlugRelatedField(slug_field="lang", read_only=True, many=True)
    genre = serializers.SlugRelatedField(slug_field="genre", read_only=True, many=True)

    class Meta:
        model = Group
        fields = (
            'name', 'language', 'year',
            'genre', 'image', 'slug',

        )


class SongSerializer(serializers.ModelSerializer):
    album = serializers.SlugRelatedField(slug_field="title", read_only=True)
    group = serializers.SlugRelatedField(slug_field="name", read_only=True)
    character = serializers.SlugRelatedField(slug_field='char', read_only=True)

    class Meta:
        model = Song
        fields = (
            'title', 'album',
            'group', 'time_create', 'time_update',
            'slug', 'character',)