from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HalloAPIView(APIView):
    """Test APIView"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_api_view = [
            'Uses HTTP methods as functions i.e GET, POST, PATCH, PUT, DELETE',
            'it is similar to a traditional django view',
            'gives you the most control over your logic',
            'is mapped manually to URLS']

        return Response({'message': 'Hallo', 'an_apiview': an_api_view})
