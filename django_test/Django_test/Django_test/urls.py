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
from mytestweb.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('create_account_page/', create_account_page, name='create_account_page'),
    path('post_create_account/', post_create_account, name='post_create_account'),
    path('create_account_success/', post_create_account, name='create_account_success'),
    path('home_page_logged/', home_page_logged, name='home_paged_logged'),
    path('sign_in_success/', sign_in_success, name='sign_in_success'),
    path('search_bar/', search_bar, name='search_bar'),
    path('get_bar_result/', get_bar_result, name='get_bar_result'),
    path('search_heatmap/', search_heatmap, name='search_heatmap'),
    path('get_heatmap_result/', get_heatmap_result, name='get_heatmap_result'),
    path('search_keyword/', search_keyword, name='search_keyword'),
    path('get_pie_result/', get_pie_result, name='get_pie_result'),
]
