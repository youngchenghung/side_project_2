from django.shortcuts import render
from django.http import HttpResponse
import datetime
import pymysql
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # 使用非 GUI 後端
from datetime import datetime
import pandas as pd
import jieba
import csv
from collections import Counter


def draw_pie_chart(request):

    try:
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

            # 連接MySQL資料庫
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='11111111',
                db='PTT_raw_data',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

        # 讀取資料
        with conn.cursor() as cursor:
            sql ="SELECT Title FROM PTT_Gossiping_data WHERE date BETWEEN %s AND %s"
            cursor.execute(sql, (start_date, end_date))
            result = cursor.fetchall()
        
        # 將資料寫入CSV檔
        with open(os.getcwd() + '/mytestweb/jieba/temp_title_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Title'])
            for row in result:
                writer.writerow([row['Title']])

        # 讀取CSV檔轉換成DataFrame資料型態
        df = pd.read_csv(os.getcwd() + '/mytestweb/jieba/temp_title_data.csv')

        # 載入自定義字典(有意義)
        # jieba.load_userdict("dict.txt.big")  # 官方預設自定義字典
        jieba.set_dictionary(os.getcwd() + '/mytestweb/jieba/custom_names.txt')

        # 載入停用詞(無意義)
        with open(os.getcwd() + '/mytestweb/jieba/stop_words.txt', "r", encoding="utf-8") as f:
            stopwords = f.read().splitlines()

        # Title欄位的資料指向texts
        texts = df['Title'].tolist()

        # 建立空列表，儲存分詞後的文本
        # 迴圈每個文本，對其進行分詞並過濾停用詞和單個字的詞語，然後連接成字符串，存入segmented_texts中
        segmented_texts = []
        for text in texts:
            # 使用結巴分詞進行文字拆解
            segmented_words = jieba.cut(text, use_paddle=True)
            # 過濾停用詞和單個字的詞語
            filtered_segmented_words = []
            for word in segmented_words:
                if word not in stopwords and len(word) > 1:
                    filtered_segmented_words.append(word)

            # 處理詞語後存入segmented_texts中
            segmented_string = ' '.join(filtered_segmented_words)
            segmented_texts.append(segmented_string)

        # 刪除詞語只出現過一次
        all_words = ' '.join(segmented_texts).split()
        word_counts = Counter(all_words)
        filtered_words = [word for word in all_words if word_counts[word] > 1]

        # 將分詞後的資料存入DataFrame欄位中的segmented_content
        df['segmented_content'] = segmented_texts
        # print(df.head())  # 顯示前5筆資料

        # 統計詞頻
        word_counts = Counter(filtered_words)

        # 統計數量最多的前10個詞語
        top_10_word_counts = word_counts.most_common(10)
        # print(type(word_counts.most_common(10)))

        # 將分詞後的資料存入CSV檔
        df.to_csv(os.getcwd() + '/mytestweb/jieba/segmented_output.csv', index=False)

        # 將top_10_word_counts[0]放入list_words
        list_words = []
        list_counts =[]

        for i in range(10):
            list_words.append(top_10_word_counts[i][0])
            list_counts.append(top_10_word_counts[i][1])
        
        # print(list_words)
        # print(list_counts)



        # list_words = (list(sort_counts['Word'][0:10]))
        # list_counts = (list(sort_counts['Counts'][0:10]))
        plt.figure(figsize=(9,5))
        plt.rcParams["font.family"] = 'Arial Unicode MS'
        separeted = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
        plt.pie(list_counts,                           # 數值
                labels = list_words,                # 標籤
                autopct = "%1.1f%%",            # 將數值百分比並留到小數點一位
                explode = separeted,            # 設定分隔的區塊位置
                pctdistance = 0.6,              # 數字距圓心的距離
                textprops = {"fontsize" : 12},  # 文字大小
                shadow=True)                    # 設定陰影


        plt.axis('equal')                                          # 使圓餅圖比例相等
        plt.title(f"{month}份在PTT前10熱門關鍵字", {"fontsize" : 20})  # 設定標題及其文字大小
        plt.legend(loc = "best")                                   # 設定圖例及其位置為最佳
        plt.show()


        file_name = f"pie_{datetime.now().strftime('%Y%m%d_%s')}.png"
        file_path =os.getcwd() + '/mytestweb/static/matplotlib_file/' + file_name

        plt.savefig(file_path)
        plt.close()
        file_url = f'/static/matplotlib_file/{file_name}'

        return file_url

    except Exception as e:
        print(e)

    finally:
        conn.close()