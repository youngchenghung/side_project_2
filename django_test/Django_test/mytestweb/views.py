from django.shortcuts import render
from django.http import HttpResponse
import pymysql
from mytestweb.module import search_category_bar, search_article_count, search_top_keyword


# Create your views here.

def index(request):
    return render(request, 'home_page.html')

def create_account_page(request):
    return render(request, 'create_account_page.html')

def post_create_account(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 連接MySQL資料庫
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='11111111',
            db='PTT_raw_data',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        # 插入數據到數據庫
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO PTT_user_account (name, sex, age, email, password) 
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (name, sex, age, email, password))
            conn.commit()

        return render(request, 'create_account_success.html')
    else:
        return render(request, 'create_account_page.html')

def home_page_logged(request):
    return render(request, 'home_page_logged.html')

def sign_in_success(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email, password)

        # 連接MySQL資料庫
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='11111111',
            db='PTT_raw_data',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with conn.cursor() as cursor:
            sql = """SELECT email, password FROM PTT_user_account WHERE email = %s"""
            cursor.execute(sql, (email))
            conn.commit()
            data = cursor.fetchall()

        # Check if the user exists
        if data is None or len(data) == 0:
            return 'Invalid email or password'
        else:
            user = data[0]
            print(user)

            # Check if the password is correct
            if user['password'] != password:
                return 'Invalid email or password'
            else:
                return render(request, 'sign_in_success.html')

def search_bar(request):
    return render(request, 'search_bar.html')

def get_bar_result(request):
    # module/search_category_bar/draw_bar_chart
    file_url = search_category_bar.draw_bar_chart(request)

    return render(request, 'search_bar.html', {'file_url': file_url})

def search_heatmap(request):
    return render(request, 'search_heatmap.html')

def get_heatmap_result(request):
    # module/search_article_count/draw_heatmap
    file_url = search_article_count.draw_heatmap(request)

    return render(request, 'search_heatmap.html', {'file_url': file_url})

def search_keyword(request):
    return render(request, 'search_keyword.html')

def get_pie_result(request):
    # module/search_top_keyword/draw_pie_chart
    file_url = search_top_keyword.draw_pie_chart(request)

    return render(request, 'search_keyword.html', {'file_url': file_url})