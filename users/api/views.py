from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken

from users.api.pagination import ListPagination
from users.api.permissions import UserViewSetPermissions
from users.api.serializers import UserSerializer


class TokenLoginView(ObtainAuthToken):
    """
    This view expands ObtainAuthToke with update last login functionality
    """

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        update_last_login(None, token.user)
        return response


class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset that provides simple CRUD on User model
    """

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    pagination_class = ListPagination
    permission_classes = [UserViewSetPermissions, ]
