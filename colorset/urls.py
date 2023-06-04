from django.urls import path
from . import views

app_name = 'colorset'
urlpatterns = [
    path('',views.colorSetPost,name='colorset'),
    path('loadrecommendset/<str:colorstr>',views.findRecommendColorSet,name='loadsetrecommendcolorsetlist'),
    path('loadset/<int:pk>',views.findMyColorSet,name='loadsetmycolorsetlist'),
    path('deleteset/<int:pk>',views.deleteColorSet,name='deleteset')
]