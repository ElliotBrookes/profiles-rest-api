from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


from profiles_api import serializers


class HelloApiView(APIView):
    """Test api view."""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of api view feature."""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'gives you the most control over your application logic',
            'is mapped manually to urls',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message using our name."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}.'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset."""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""
        a_viewset = [
            "uses actions for a viewset (CRUD)",
            "automatically maps to urls using routers",
            "more functionality with less code"
        ]

        return Response({'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an objkect via id."""
        return Response({"HTTP": 'GET'})

    def update(self, request, pk=None):
        """Handle updating an objecdt."""
        return Response({"HTTP": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object."""
        return Response({"HTTP": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle removing an object."""
        return Response({"HTTP": "DELETE"})
