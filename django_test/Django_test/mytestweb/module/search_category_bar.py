from django.shortcuts import render
from django.http import HttpResponse
import datetime
import pymysql
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # 使用非 GUI 後端
from datetime import datetime
import seaborn as sns
import pandas as pd
from collections import Counter

def draw_bar_chart(request):


    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        month = request.GET.get('month')

        if month == ('一月'):
            start_date = 100 + int(start_date)
            end_date = 100 + int(end_date)
        elif month == ('二月'):
            start_date = 200 + int(start_date)
            end_date = 200 + int(end_date)
        elif month == ('三月'):
            start_date = 300 + int(start_date)
            end_date = 300 + int(end_date)
        elif month == ('四月'):
            start_date = 400 + int(start_date)
            end_date = 400 + int(end_date)
        elif month == ('五月'):
            start_date = 500 + int(start_date)
            end_date = 500 + int(end_date)
        elif month == ('六月'):
            start_date = 600 + int(start_date)
            end_date = 600 + int(end_date)
        elif month == ('所有'):
            start_date = 100 + int(start_date)
            end_date = 600 + int(end_date)


        # print(f"start_date: {start_date}, end_date: {end_date}")
            

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
        conn.commit()
        results = cursor.fetchall()


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
            conn.commit()
            results = cursor.fetchall()
        
    # print(results)

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
    plt.xlabel('文章類別')
    plt.ylabel('文章數量（篇）')
    plt.title(f'PTT八卦版 {month}文章類別長條圖')
    
    file_name = f"plot_{datetime.now().strftime('%Y%m%d')}.png"
    file_path =os.getcwd() + '/mytestweb/static/matplotlib_file/' + file_name

    plt.savefig(file_path)
    plt.close()
    file_url = f'/static/matplotlib_file/{file_name}'

    return file_url