from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HalloSerializer


# Create your views here.
class HalloAPIView(APIView):
    """Test APIView"""

    serializer_class = HalloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_api_view = [
            'Uses HTTP methods as functions i.e GET, POST, PATCH, PUT, DELETE',
            'it is similar to a traditional django view',
            'gives you the most control over your logic',
            'is mapped manually to URLS']

        return Response({'message': 'Hallo', 'an_apiview': an_api_view})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = HalloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hallo {name}'

            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)  # invalid data
