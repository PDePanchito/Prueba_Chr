"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from api_v1.views import apiGet
from api_v1.views import storeData
from api_v1.views import databaseGet
from selenium_script.views import view_data
from selenium_script.views import view_table

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', apiGet, name='api'),
    path('api-store/', storeData, name='api-store'),
    path('bootstrapview', databaseGet, name='bootstrapview'),
    path('scrape-data/', view_data, name='scrape-data'),
    path('scrape-view/', view_table, name='scrape-view')

]
