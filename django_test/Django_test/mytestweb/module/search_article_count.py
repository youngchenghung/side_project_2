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

def draw_heatmap(request):
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
        SELECT Pop, 
        Date 
        FROM PTT_Gossiping_data 
        WHERE Date BETWEEN %s AND %s
        """
        cursor.execute(sql, (start_date, end_date))
        results = cursor.fetchall()
        conn.commit()

        processed_results = [
            {
            'Pop': result['Pop'],
            'Month': result['Date'][:-2],
            'Day': result['Date'][-2:]
            }
            for result in results
        ]

    # 將資料庫資料轉換成適合繪製熱力圖的格式
    df = pd.DataFrame(processed_results, columns=['Pop', 'Month', 'Day'])
    heatmap_data = df.pivot_table(index='Month', columns='Day', values='Pop', aggfunc='sum', fill_value=0)

    # 繪製熱力圖
    plt.rcParams["font.family"] = 'Arial Unicode MS'
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data,  fmt="d", cmap='coolwarm')
    plt.title(f'{start_date}至{end_date}文章數的熱力圖表') 
    plt.yticks(rotation=0)
    plt.ylabel('單位：月')
    plt.xlabel('單位：日')
    plt.show()

    file_name = f"heatmap_{datetime.now().strftime('%Y%m%d_%s')}.png"
    file_path =os.getcwd() + '/mytestweb/static/matplotlib_file/' + file_name

    plt.savefig(file_path)
    plt.close()
    file_url = f'/static/matplotlib_file/{file_name}'

    return file_url