from django.urls import include, path
from rest_framework import routers

from .views import FilmViewSet


router = routers.DefaultRouter()
router.register('films', FilmViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
]
