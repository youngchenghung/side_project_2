from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import datetime
import pymysql


# Create your views here.

def index(request):
    web_name = "Leo Django web site"
    article_list = [{'title':"Django web site", 'author':"Leo", 'date':datetime.datetime.strptime("2024-04-27", "%Y-%m-%d")},
                    {'title':"test web site 1", 'author':"Tom", 'date':datetime.datetime.strptime("2024-04-28", "%Y-%m-%d")},
                    {'title':"test web site 2", 'author':"Jack", 'date':datetime.datetime.strptime("2024-04-29", "%Y-%m-%d")},]
    return render(request, 'home_page.html', context={'web_name':web_name, 'article_list':article_list})

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
        conn = pymysql.connect(host='localhost', user='root', password='11111111', db='PTT_raw_data')

        try:
            with conn.cursor() as cursor:
                use = "USE PTT_raw_data"
                sql = "SELECT * FROM PTT_Gossiping_data WHERE Title LIKE %s"
                value = "%"+title+"%"
                cursor.execute(use)
                cursor.execute(sql, (value))
                conn.commit()
            
                result = cursor.fetchall()
                print(result)  # 確認是否有數據
                if not result:
                    return HttpResponse("No results found.")

                # print(data_list)

            return render(request, 'search_results.html', {'result': result})
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")
        finally:
            conn.close()
    else:
        return HttpResponse("Invalid request method.")



def page_4(request):
    return render(request, 'page_4.html')