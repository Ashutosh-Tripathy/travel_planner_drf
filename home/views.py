from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import Travel
from .serializers import TravelSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .permissions import IsAdminOrSelf, IsAdminOrManagerOrSelf, UserPermission

# Create your views here.

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = (IsAuthenticated, IsAdminOrSelf)

class TravelList(generics.ListCreateAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = (IsAuthenticated, IsAdminOrSelf)



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission, )


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission, )
