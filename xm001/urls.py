"""xm001 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app01 import views as app01_views
from webapp01 import views as cal_views

urlpatterns = [
    path("", app01_views.home, name='home'),
    path('add/', cal_views.add, name='add'),
    path('add/<int:a>/<int:b>/', cal_views.old_add_redirect),
    path('newadd/<int:a>/<int:b>/', cal_views.add2, name='add2'),
    path('admin/', admin.site.urls),
]
