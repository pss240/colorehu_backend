from django.urls import path
from . import views

app_name = 'colorset'
urlpatterns = [
    path('',views.colorSetPost,name='colorset'),
    path('loadSet',views.findColorSet,name='loadset'),
]