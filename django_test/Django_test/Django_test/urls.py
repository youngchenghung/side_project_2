"""
URL configuration for Django_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from mytestweb.views import index, page_2, insert_data, search_title, search_bar, get_bar_result, search_heatmap, get_heatmap_result, search_keyword, get_pie_result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('page_2/', page_2),
    # path('page_3/', page_3),
    # path('page_4/', page_4),
    path('insert_data/' , insert_data, name='insert_data'),
    path('search_title/', search_title, name='search_title'),
    path('search_bar/', search_bar, name='search_bar'),
    path('get_bar_result/', get_bar_result, name='get_bar_result'),
    path('search_heatmap/', search_heatmap, name='search_heatmap'),
    path('get_heatmap_result/', get_heatmap_result, name='get_heatmap_result'),
    path('search_keyword/', search_keyword, name='search_keyword'),
    path('get_pie_result/', get_pie_result, name='get_pie_result'),
]
