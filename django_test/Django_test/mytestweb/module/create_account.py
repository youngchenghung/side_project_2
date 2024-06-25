from django.shortcuts import render
from django.http import HttpResponse
import pymysql

def user_create_account(request):
    try: 
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

            redirect_success_url = 'create_account_success.html'
            return redirect_success_url
        else:
            redirect_unsuccess_url = 'create_account_page.html'
            return redirect_unsuccess_url
        
    except Exception as e:
        print(e)
        
    finally:
        conn.close()