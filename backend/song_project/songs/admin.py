from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'language', 'time_create', 'time_update')


admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Song)