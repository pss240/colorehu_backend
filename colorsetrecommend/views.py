import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from colorsetrecommend.serializer import ColorsetrecommendSerializer



@api_view(['POST'])
def post(request):
    print("inside of colorsetrecommend in")
    if request.method == 'POST':
        serializer = ColorsetrecommendSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)

    return Response(serializer.errors,status=400)
    