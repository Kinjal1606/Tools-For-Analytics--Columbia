"""tfa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from sightings.views import map, list_sighting, squirrel_add_new, squirrel_update_existing, squirrel_stats ### function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', map),
    path('sightings/',list_sighting),
    path('sightings/add/', squirrel_add_new),
    path('sightings/<str:unique_id>/', squirrel_update_existing),
    path('stats/', squirrel_stats)


]
