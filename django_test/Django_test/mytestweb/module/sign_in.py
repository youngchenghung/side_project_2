from django.http import HttpResponse
import pymysql

def user_sign_in(request):
    try:
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

            # 查詢數據庫
            with conn.cursor() as cursor:
                sql = """SELECT email, password FROM PTT_user_account WHERE email = %s"""
                cursor.execute(sql, (email))
                conn.commit()
                data = cursor.fetchall()

            # 檢查用戶是否存在
            if data is None or len(data) == 0:
                return 'Invalid email or password'
            else:
                user = data[0]
                print(user)

                # 檢查密碼是否正確
                if user['password'] != password:
                    return 'Invalid email or password'
                else:
                    redirect_success_url = 'sign_in_success.html'
                    return redirect_success_url
                
    except Exception as e:
        print(e)

    finally:
        conn.close()