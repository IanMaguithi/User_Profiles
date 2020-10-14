from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from .views import HalloAPIView, HalloViewsets

router = DefaultRouter()
router.register('hallo-viewset', HalloViewsets, basename='hallo-viewset')

urlpatterns = [
    path('Hallo-View/', HalloAPIView.as_view()),
    path('', include(router.urls))
]
