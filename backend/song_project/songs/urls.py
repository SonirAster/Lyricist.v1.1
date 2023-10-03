from django.urls import path, include
from rest_framework import routers

from songs.views import *


router_group = routers.SimpleRouter()
router_group.register(r'group', GroupViewSet, basename='group')


router_main = routers.SimpleRouter()
router_main.register(r'', MainPageViewSet, basename='')


urlpatterns = [
    path('', include(router_group.urls)),
    path('', include(router_main.urls)),

]