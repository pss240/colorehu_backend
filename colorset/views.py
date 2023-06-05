import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from colorset.models import ColorSet
from colorset.serializer import ColorSetSerializer
from django.core import serializers

from signin.models import Signin



@api_view(['POST'])
def colorSetPost(request):
    print("inside of colorset in")
    if request.method == 'POST':
        print("aaaaaaaa")
        serializer = ColorSetSerializer(data=request.data)
        print("abbbbbbbbbbbbbb")
        if serializer.is_valid():
            print("cccccccccccccccccc")
            serializer.save()
            return Response(serializer.data,status=200)
    print("addddddddddddddddd")
    return Response(serializer.errors,status=400)

@api_view(['GET'])
def findRecommendColorSet(request,colorstr,keyword):
    
    colorSetQuery = ColorSet.objects.all().filter(keyword = keyword)
    colorSetQuery = colorSetQuery.filter(colorsetstr__contains=colorstr)
    colorSetQuery = colorSetQuery.filter(share=True)
    serialized_colorSet = ColorSetSerializer(colorSetQuery,many=True)
    
    return Response(serialized_colorSet.data,status=200)

@api_view(['GET'])
def findMyColorSet(request,pk):
    print("inside of findMyColorSet")
    colorSetQuery = ColorSet.objects.all().filter(uid=pk)
    serialized_colorSet = ColorSetSerializer(colorSetQuery,many=True)
    
    return Response(serialized_colorSet.data,status=200)

@api_view(['GET'])
def deleteColorSet(request,pk):
    ColorSet.objects.get(pk = pk).delete()
    return Response(status=200)
        
    