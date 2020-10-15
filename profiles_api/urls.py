from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from .views import HalloAPIView, HalloViewsets, UserProfileViewSet

router = DefaultRouter()
router.register('hallo-viewset', HalloViewsets, basename='hallo-viewset')
router.register('profile', UserProfileViewSet)  # model view_set, no need for basename as django rest can figure it out

urlpatterns = [
    path('Hallo-View/', HalloAPIView.as_view()),
    path('', include(router.urls))
]
