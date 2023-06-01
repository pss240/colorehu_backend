import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from .models import Signin
# Create your views here.

class SigninView(View):
    def get(self,request):
        dummy_data = {
            'nickname':'parkchanyoung',
            'email':'qjadjehd05@gmail.com'
        }
        return JsonResponse(dummy_data)
    
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
    
    def put(self,request):
        return HttpResponse("put요청을 잘 받았다")
    
    def delete(self,request):
        return HttpResponse("delete요청을 잘 받았다")
    