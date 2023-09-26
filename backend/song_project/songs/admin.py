from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('lang',)


@admin.register(Genre)
class Genre(admin.ModelAdmin):
    list_display = ('genre',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'language', 'get_image', 'time_create', 'time_update', )
    list_display_links = ('name', 'id',)
    readonly_fields = ('time_create', 'time_update', 'language', 'get_image',)
    search_fields = ('name', 'year', 'language__lang',)
    list_filter = ('year', 'language__lang',)
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None, {
            'fields': (('name', 'slug',),)
        }),
        (None, {
            'fields': (('genre', 'language',),)
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
    list_display = ('title', 'year', 'get_image', 'group',)
    list_display_links = ('title', 'group')
    search_fields = ('title', 'year',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='100'")

    get_image.short_description = "Image"


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'year', 'group', 'album',
        'time_create', 'time_update', 'is_published',
    )
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'year', 'group__name', 'album__title')
    list_editable = ('is_published',)
    readonly_fields = ('time_create', 'time_update',)
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'),)
        }),
        (None, {
            'fields': (('group', 'album'),)
        }),
        (None, {
            'fields': (('year', 'is_published',),)
        }),
        (None, {
            'fields': (('time_create', 'time_update'),)
        }),
    )


