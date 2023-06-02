from django.urls import path
from . import views

app_name = 'colorsetrecommend'
urlpatterns = [
    path('',views.post,name='colorsetrecommend'),
]