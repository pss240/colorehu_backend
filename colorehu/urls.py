
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin',include('signin.urls')),
    path('colorsetrecommend',include('colorsetrecommend.urls')),
]
