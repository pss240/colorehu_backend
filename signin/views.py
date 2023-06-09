import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from signin.serializer import SigninSerializer

from .models import Signin
# Create your views here.

@api_view(['GET'])
def get(request):
    print("inside of sign in get")
    user = Signin.objects.all()
    serialized_user = SigninSerializer(user, many=True)
    return Response(serialized_user.data,status=200)

@api_view(['POST'])
def post(request):
    print("inside of sign in")

    if request.method == 'POST':
        serializer = SigninSerializer(data=request.data)
        try:
            if serializer.is_valid():
                duplicate = Signin.objects.all().get(email=serializer.validated_data['email'])
                serializer = SigninSerializer(duplicate)
                return Response(serializer.data,status=200)
        except:
           if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=200)
    return Response(serializer.errors,status=400)
    

@api_view(['GET'])
def change_nickname(request,pk,nickname):
    try:
        duplicate = Signin.objects.all().get(nickname=nickname)
    except:
        duplicate = None
    if duplicate==None:
        changeUser = Signin.objects.all().get(pk=pk)
        changeUser.nickname = nickname
        changeUser.save()
        serialized_user = SigninSerializer(changeUser)
        return Response(serialized_user.data,status=200)
    else:
        return Response({'jsonStatus':400},status=400)
    