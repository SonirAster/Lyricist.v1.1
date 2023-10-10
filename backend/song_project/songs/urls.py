from django.urls import path, include
from rest_framework import routers

from .views import *


router_group = routers.SimpleRouter()
router_group.register(r'group', GroupViewSet, basename='group')


router_main = routers.SimpleRouter()
router_main.register(r'', MainPageViewSet, basename='')


urlpatterns = [
    path('', include(router_group.urls)),
    path('recently-added/', include(router_main.urls)),
    path('character/', CharacterView.as_view()),
    path('language/', LanguageView.as_view()),
    path('genre/', GenreView.as_view()),
]