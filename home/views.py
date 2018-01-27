from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import Travel
from .serializers import TravelSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class TravelList(generics.ListAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = (IsAuthenticated,)

class TravelList(generics.ListCreateAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = (IsAuthenticated,)
