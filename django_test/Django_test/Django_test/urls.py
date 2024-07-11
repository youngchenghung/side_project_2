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
from mytestweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index),
    path('create_account_page/', views.create_account_page, name='create_account_page'),
    path('post_create_account/', views.post_create_account, name='post_create_account'),
    path('create_account_success/', views.post_create_account, name='create_account_success'),
    path('home_page_logged/', views.home_page_logged, name='home_paged_logged'),
    path('sign_in_success/', views.sign_in_success, name='sign_in_success'),
    path('search_bar/', views.search_bar, name='search_bar'),
    path('get_bar_result/', views.get_bar_result, name='get_bar_result'),
    path('search_heatmap/', views.search_heatmap, name='search_heatmap'),
    path('get_heatmap_result/', views.get_heatmap_result, name='get_heatmap_result'),
    path('search_keyword/', views.search_keyword, name='search_keyword'),
    path('get_pie_result/', views.get_pie_result, name='get_pie_result'),

    path('orm/user_info_list/', views.orm_user_info_list, name='orm_user_info_list'),
    path('orm/user_add/', views.orm_user_add, name='orm_user_add'),
    path('orm/user_delete/', views.orm_user_delete, name='orm_user_delete'),

    path('orm/orm_department_info_list/', views.orm_department_info_list, name='orm_department_info_list'),
    path('orm/orm_department_add/', views.orm_department_add, name='orm_department_add'),
    path('orm/orm_department_edit/<int:nid>/', views.orm_department_edit, name='orm_department_edit'),
    path('orm/orm_department_delete/', views.orm_department_delete, name='orm_department_delete'),

    path('orm/modelform_add_user/', views.modelform_add_user, name='modelform_add_user'),
    path('orm/modelform_user_edit/<int:nid>/', views.modelform_user_edit, name='modelform_user_edit'),

    path('admin_account/', views.admin_account, name='admin_account'),
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
]
