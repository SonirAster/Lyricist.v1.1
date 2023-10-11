from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('char',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('lang',)


@admin.register(Genre)
class Genre(admin.ModelAdmin):
    list_display = ('genre',)


@admin.register(Year)
class Year(admin.ModelAdmin):
    list_display = ('year',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'get_image', 'time_create', 'time_update', )
    list_display_links = ('name', 'id',)
    readonly_fields = ('time_create', 'time_update', 'get_image',)
    search_fields = ('name', 'year', 'language__lang',)
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None, {
            'fields': (('name', 'slug', 'description',),)
        }),
        (None, {
            'fields': (('genre', 'language', 'character',),)
        }),
        (None, {
            'fields': (('year', 'time_create', 'time_update'),)
        }),
        (None, {
            'fields': (('image', 'get_image'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='100'")

    get_image.short_description = "Image"


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title',  'get_image', 'group',)
    list_display_links = ('title', 'group')
    readonly_fields = ('get_image',)
    search_fields = ('title', 'year',)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='100'")

    get_image.short_description = "Image"


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title',
        'group', 'album',
        'time_create', 'time_update', 'is_published',

    )
    list_display_links = ('title',)
    readonly_fields = ('time_create', 'time_update',)
    search_fields = ('title', 'group__name', 'album__title',)
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {
            'fields': (('title', 'slug', 'text'),)
        }),
        (None, {
            'fields': (('group', 'album'),)
        }),
        (None, {
            'fields': (( 'is_published', 'character',),)
        }),
        (None, {
            'fields': (('time_create', 'time_update'),)
        }),
    )

