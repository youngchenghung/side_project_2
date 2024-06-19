from django.shortcuts import render
from django.http import HttpResponse
import pymysql
from mytestweb.module import search_category_bar, search_article_count, search_top_keyword


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
                sql = """INSERT INTO PTT_Gossiping_data (category, title, pop, author, date, current_page_index) VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (category, title, pop, author, date, current_page_index))
                conn.commit()
            return HttpResponse("Data inserted successfully!")
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")
        finally:
            conn.close()
    else:
        return HttpResponse("Invalid request method.")


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
                sql = """SELECT * FROM PTT_Gossiping_data WHERE Title LIKE %s"""
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