from django.shortcuts import render
from django.http import HttpResponse
import pymysql
from mytestweb.module import create_account, sign_in, search_category_bar, search_article_count, search_top_keyword 


# Create your views here.

def index(request):
    return render(request, 'home_page.html')

def create_account_page(request):
    return render(request, 'create_account_page.html')

def post_create_account(request):
    # module/create_account/user_create_account
    url = create_account.user_create_account(request)

    # 回傳網址
    return render(request, url)

def home_page_logged(request):
    return render(request, 'home_page_logged.html')

def sign_in_success(request):
    # module/sign_in/user_sign_in
    url = sign_in.user_sign_in(request)

    # 回傳網址
    return render(request, url)

def search_bar(request):
    return render(request, 'search_bar.html')

def get_bar_result(request):
    # module/search_category_bar/draw_bar_chart
    file_url = search_category_bar.draw_bar_chart(request)

    # 回傳圖片網址
    return render(request, 'search_bar.html', {'file_url': file_url})

def search_heatmap(request):
    return render(request, 'search_heatmap.html')

def get_heatmap_result(request):
    # module/search_article_count/draw_heatmap
    file_url = search_article_count.draw_heatmap(request)

    # 回傳圖片網址
    return render(request, 'search_heatmap.html', {'file_url': file_url})

def search_keyword(request):
    return render(request, 'search_keyword.html')

def get_pie_result(request):
    # module/search_top_keyword/draw_pie_chart
    file_url = search_top_keyword.draw_pie_chart(request)

    # 回傳圖片網址
    return render(request, 'search_keyword.html', {'file_url': file_url})