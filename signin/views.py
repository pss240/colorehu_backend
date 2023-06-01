import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from .models import Signin
# Create your views here.

@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        request = json.loads(request.body)
        user = Signin(nickname = request['nickname'],
                        email = request['email'])
    else:
        user = Signin(nickname = request.POST['nickname'],
                        email = request.POST['email'])
    user.save()
    return HttpResponse(status=200)
    