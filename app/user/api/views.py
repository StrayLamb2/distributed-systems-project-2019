from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
    permission_classes = ()


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer

    # Sets the renderer so we can view the endpoint
    # in the browsable api
    # If we ever want to change the api renderer
    # we can do so by adding a new renderer class inside
    # the project settings
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    # overriding get_object
    def get_object(self):
        """Retrieve and return authenticated user"""
        # when get_object is called, the request will have
        # the user attached to is because of the authentication_classes
        # that takes care of taking the authenticated user and
        # assigning him/her to the request
        return self.request.user
