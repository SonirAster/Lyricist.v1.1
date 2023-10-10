from rest_framework import serializers

from .models import *


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    language = serializers.SlugRelatedField(slug_field='lang', read_only=True, many=True)
    genre = serializers.SlugRelatedField(slug_field='genre', read_only=True, many=True)
    character = serializers.SlugRelatedField(slug_field='char', read_only=True, )

    class Meta:
        model = Group
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(slug_field='name', read_only=True,)
    album = serializers.SlugRelatedField(slug_field='title', read_only=True,)
    character = serializers.SlugRelatedField(slug_field='char', read_only=True, )

    class Meta:
        model = Song
        fields = '__all__'


