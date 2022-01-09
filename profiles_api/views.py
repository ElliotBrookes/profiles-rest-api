from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view."""

    def get(self, request, format=None):
        """Returns a list of api view feature."""

        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'gives you the most control over your application logic',
            'is mapped manually to urls',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
