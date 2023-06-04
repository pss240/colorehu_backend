from django.urls import path
from . import views

app_name = 'colorset'
urlpatterns = [
    path('',views.colorSetPost,name='colorset'),
    path('loadset/<str:colorstr>',views.findRecommendColorSet,name='loadsetrecommendcolorsetlist'),
    path('loadset/<int:id>',views.findMyColorSet,name='loadsetmycolorsetlist'),
    path('deleteset/<int:pk>',views.deleteColorSet,name='deleteset')
]