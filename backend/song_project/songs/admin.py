from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Group)
admin.site.register(Album)
admin.site.register(Song)