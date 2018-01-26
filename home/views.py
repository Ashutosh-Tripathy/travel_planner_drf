from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Travel
from .serializers import TravelSerializer

# Create your views here.



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



def travel_list(request):
    if request.method == 'GET':
        travels = Travel.objects.all()
        serializer = TravelSerializer(travels, many=True)
        return JSONResponse(serializer.data)
