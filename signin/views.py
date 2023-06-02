import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from signin.serializer import SigninSerializer

from .models import Signin
# Create your views here.

@api_view(['POST'])
def post(request):
    print("inside of sign in post")
    if request.META['CONTENT-TYPE'] == 'application/json':
        serializer = SigninSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)

    return Response(serializer.errors,status=400)
    