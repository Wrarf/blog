from django.contrib.auth import get_user_model
from rest_framework import viewsets
from auth.serializers import UserSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer