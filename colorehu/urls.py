
from django.contrib import admin
from django.urls import include, path

import signin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/',include(signin.urls)),
]
