import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

import Signin

# Create your views here.

class SigninView(View):
    def post(self,request):
        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)
            user = Signin(nickname = request['nickname'],
                          email = request['email'])
        else:
            user = Signin(nickname = request.POST['nickname'],
                          email = request.POST['email'])
        user.save()
        return HttpResponse(status=200)