from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import serializer
from . import models
from . import permission


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


class Helloviewset(viewsets.ViewSet):
    """Test API viewset."""
    serializer_class = serializer.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
        'Uses actions (list, create, retirieve, update, partial_update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code.'
        ]

        return Response({'message':'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        # create a new serializer request
        serializers = serializer.HelloSerializer(data=request.data)
        #check if serializers is valid
        if serializers.is_valid():
            name = serializers.data.get('name')
            message = 'Hello {0}'.format(name)

            return Response({'message':message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def retrieve(self, request, pk=None):
        """Handles getting object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """update an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of the object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating,listing and updating profiles."""
    serializer_class = serializer.UserProfileSeriliazer
    queryset = models.UserProfile.objects.all()
    #add token authentication using a tuple which contains other authentication classes
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateProfile,)
