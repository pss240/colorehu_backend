from django.urls import path
from . import views

app_name = 'signin'
urlpatterns = [
    path('',views.post,name='signin'),
    path('get',views.get,name='signin_get'),
]