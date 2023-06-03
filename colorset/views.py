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

@api_view(['POST'])
def findColorSet(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        setstr = json_data['str']
        colorSetQuery = ColorSet.objects.all().filter(colorsetstr__contains=setstr)
        colorSetJson = serializers.serialize("json",colorSetQuery)
        
        return JsonResponse(colorSetJson,status=200)
        
    