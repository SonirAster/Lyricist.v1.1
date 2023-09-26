from django.urls import path, include
from rest_framework import routers

from songs.views import *

router_main = routers.SimpleRouter()
router_main.register(r'', MainPageViewSet, basename='')
print(router_main.urls)

router_group = routers.SimpleRouter()
router_group.register(r'group', GroupViewSet, basename='group')
print(router_group.urls)

urlpatterns = [
    path('', include(router_main.urls)),
    path('', include(router_group.urls)),

]