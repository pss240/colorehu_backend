import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from colorset.models import ColorSet
from colorset.serializer import ColorSetSerializer
from django.core import serializers



@api_view(['POST'])
def colorSetPost(request):
    print("inside of colorset in")
    if request.method == 'POST':
        serializer = ColorSetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)

    return Response(serializer.errors,status=400)

@api_view(['GET'])
def findColorSet(request,colorstr):
    
    colorSetQuery = ColorSet.objects.all().filter(colorsetstr__contains=colorstr)
    serialized_colorSet = ColorSetSerializer(colorSetQuery,many=True)
    
    return Response(serialized_colorSet.data,status=200)
        
    