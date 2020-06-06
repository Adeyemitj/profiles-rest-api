from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .import serializer


# Create your views here.

class HelloView(APIView):
    """Test API View"""
    serializer_class = serializer.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
        'Uses HTTP methods as functions (get, post, patch, put, delete)',
        'It is similar to a traditional Django view',
        'Gives you the most control over your logic',
        'It append normally to URLs'
        ]

        return Response({'message':'Hello', 'an_apiView':an_apiview})

    # make a HTTP-POST request for the APIView
    def post(self, request):
        """Create a hello message with our name """
        serializers = serializer.HelloSerializer(data=request.data)

        # validate that data posted is valid in the serializer
        if serializers.is_valid():
            name = serializers.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """Handles updating an objects"""

        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method':'delete'})
