from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import datetime
import pymysql
import io
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # 使用非 GUI 後端
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from django.http import HttpResponse
from datetime import datetime
from collections import Counter


# Create your views here.

def index(request):
    return render(request, 'home_page.html')

def page_2(request):
    return render(request, 'page_2.html')  

def insert_data(request):
    # 請求方法為GET時，取得前端傳來的資料
    if request.method == 'GET':
        category = request.GET.get('category')
        title = request.GET.get('title')
        pop = request.GET.get('pop')
        author = request.GET.get('author')
        date = request.GET.get('date')
        current_page_index = request.GET.get('current_page_index')
        print(f"category: {category}, title: {title}, pop: {pop}, author: {author}, date: {date}, current_page_index: {current_page_index}")
        
        # 連接MySQL資料庫
        conn = pymysql.connect(host='localhost', user='root', password='11111111', db='PTT_raw_data')

        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO PTT_Gossiping_data (category, title, pop, author, date, current_page_index) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (category, title, pop, author, date, current_page_index))
                conn.commit()
            return HttpResponse("Data inserted successfully!")
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")
        finally:
            conn.close()
    else:
        return HttpResponse("Invalid request method.")

def page_3(request):
    return render(request, 'page_3.html')


def search_title(request):
    if request.method == 'GET':
        title = request.GET.get('title')
        print(f"title: {title}")

        # 連接MySQL資料庫
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='11111111',
            db='PTT_raw_data',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM PTT_Gossiping_data WHERE Title LIKE %s"
                value = "%" + title + "%"
                cursor.execute(sql, (value,))
                result = cursor.fetchall()
                print(result)  # 確認是否有數據

            return render(request, 'search_title.html', {'results': result})
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")
        finally:
            conn.close()
    else:
        return HttpResponse("Invalid request method.")



def page_4(request):
    return render(request, 'page_4.html')

def plot_category(request):

    file_url = None


    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        
        # 確認用戶輸入
        if not start_date or not end_date:
            return HttpResponse("Invalid input.")

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
        sql = """
        SELECT Category FROM PTT_Gossiping_data
        WHERE Date BETWEEN %s AND %s
        """
        cursor.execute(sql, (start_date, end_date))
        results = cursor.fetchall()

    # 生成 Category 的直方圖    
    # 設定字型
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    
    # 提取 categories 並計算每個類別的數量
    filtered_categories = [
        result['Category']
        for result in results
        if result['Category'] in ['[問卦]', '[新聞]', '[爆卦]']
    ]
    
    category_counts = Counter(filtered_categories)

    # 定義類別標籤
    labels = [
        '[問卦]',
        '[新聞]',
        '[爆卦]'
    ]
    
    values = [
        category_counts.get(label, 0)
        for label in labels
    ]

    # 設定字型
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

    # 繪製條形圖
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, edgecolor='black', align='center')
    plt.title(f'Category Distribution from {start_date} to {end_date}')
    plt.xlabel('文章類別')
    plt.ylabel('文章數量（篇）')
    plt.title('PTT八卦版 一月文章類別分布')
    
    file_name = f"plot_{datetime.now().strftime('%Y%m%d')}.png"
    file_path = '/Users/leo/Documents/side_project_2-1/django_test/Django_test/mytestweb/static/' + file_name

    plt.savefig(file_path)
    plt.close()
    file_url = f'/static/{file_name}'

    return render(request, 'search_form.html', {'file_url': file_url})

def search_form(request):
    return render(request, 'search_form.html')