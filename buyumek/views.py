from django.shortcuts import render
from django.http import HttpResponse
from .models import Propiedad
from rest_framework.decorators import api_view
from .serializers import PropiedadSerializer
from rest_framework.response import Response

@api_view(['get'])
def fetch_properties(request):
    #fetch all the property objects
    properties = Propiedad.objects.all()
    #send the actor objects as a response
    serializer = PropiedadSerializer(properties, many=True) 
    return Response(serializer.data)
