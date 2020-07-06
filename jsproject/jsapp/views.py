from .models import User_Act
from jsapp.serializers import UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User_Act.objects.all()
    serializer_class = UserSerializer
