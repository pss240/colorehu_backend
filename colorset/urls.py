from django.urls import path
from . import views

app_name = 'colorset'
urlpatterns = [
    path('',views.post,name='colorset'),
]