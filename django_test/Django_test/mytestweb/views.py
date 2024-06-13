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
    conn = pymysql.connect(host='localhost')
    cursor = conn.cursor()
    query = "INSERT INTO PTT_Gossiping_data values('" + request.GET['Category']+ "','" + request.GET['Title']+ "')"
    cursor.execute(query)
    conn.commit()
    conn.close()


def page_3(request):
    return render(request, 'page_3.html')  

def page_4(request):
    return render(request, 'page_4.html')