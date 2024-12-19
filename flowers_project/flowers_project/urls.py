"""
URL configuration for flowers_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# flowers/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_gullar, name='all_gullar'),
    path('tur/<int:tur_id>/', views.gullar_by_tur, name='gullar_by_tur'),
    path('gul/<int:gul_id>/', views.gul_detail, name='gul_detail'),
]
