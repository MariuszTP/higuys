"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from pageb.views import base, main1,  main2, main, gallery1, gallery2, gallery3, gallery4, gallery5, materialy

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main1, name='main'),
    path('main2', main2, name='base'),
    path('a', main, name='main'),
    path('g1', gallery1, name='gallery11'),
    path('m', materialy, name='materialy'),
    path('g2', gallery2, name='gallery2'),
    path('g3', gallery3, name='gallery3'),
    path('g4', gallery4, name='gallery4'),
    path('g5', gallery5, name='gallery5'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

