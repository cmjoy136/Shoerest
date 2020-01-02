"""shoerest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from shoerest.quickstart.models import *

admin.site.register(Manufacturer)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)
admin.site.register(Shoe)

from rest_framework import routers

from shoerest.quickstart.views import *

router = routers.DefaultRouter()
router.register(r'manufacturer', ManufacturerView),
router.register(r'shoetype', ShoeTypeView),
router.register(r'shoecolor', ShoeColorView),
router.register(r'shoe', ShoeView)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls))
]
