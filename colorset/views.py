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
def findRecommendColorSet(request,colorstr):
    
    colorSetQuery = ColorSet.objects.all().filter(colorsetstr__contains=colorstr)
    #colorSetQuery = colorSetQuery.filter(share=True)
    serialized_colorSet = ColorSetSerializer(colorSetQuery,many=True)
    
    return Response(serialized_colorSet.data,status=200)

@api_view(['GET'])
def findMyColorSet(request,pk):
    
    colorSetQuery = ColorSet.objects.all().filter(uid=pk)
    serialized_colorSet = ColorSetSerializer(colorSetQuery,many=True)
    
    return Response(serialized_colorSet.data,status=200)

@api_view(['GET'])
def deleteColorSet(request,pk):
    ColorSet.objects.get(pk = pk).delete()
    return Response(status=200)
        
    