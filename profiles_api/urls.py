from django.urls import path

from .views import HalloAPIView

urlpatterns = [
    path('Hallo-View/', HalloAPIView.as_view()),
]
