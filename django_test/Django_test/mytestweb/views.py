from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from mytestweb.module import create_account, sign_in, search_category_bar, search_article_count, search_top_keyword 


# Create your views here.

def index(request):
    return render(request, 'home_page.html')

def create_account_page(request):
    return render(request, 'create_account_page.html')

def post_create_account(request):
    # module/create_account/user_create_account
    url = create_account.user_create_account(request)

    # 回傳網址
    return render(request, url)

def home_page_logged(request):
    return render(request, 'home_page_logged.html')

def sign_in_success(request):
    # module/sign_in/user_sign_in
    url = sign_in.user_sign_in(request)

    # 回傳網址
    return render(request, url)

def search_bar(request):
    return render(request, 'search_bar.html')

def get_bar_result(request):
    # module/search_category_bar/draw_bar_chart
    file_url = search_category_bar.draw_bar_chart(request)

    # 回傳圖片網址
    return render(request, 'search_bar.html', {'file_url': file_url})

def search_heatmap(request):
    return render(request, 'search_heatmap.html')

def get_heatmap_result(request):
    # module/search_article_count/draw_heatmap
    file_url = search_article_count.draw_heatmap(request)

    # 回傳圖片網址
    return render(request, 'search_heatmap.html', {'file_url': file_url})

def search_keyword(request):
    return render(request, 'search_keyword.html')

def get_pie_result(request):
    # module/search_top_keyword/draw_pie_chart
    file_url = search_top_keyword.draw_pie_chart(request)

    # 回傳圖片網址
    return render(request, 'search_keyword.html', {'file_url': file_url})

from mytestweb.models import UserInfo, Department

def orm(reuqest):
    # 新增department表格資料
    # Department.objects.create(depart_name='IT', depart_menber=10)
    # Department.objects.create(depart_name='HR', depart_menber=2)
    # Department.objects.create(depart_name='Sales', depart_menber=5)


    # 刪除department表格id=1的資料
    # Department.objects.filter(id=1).delete()

    # 刪除department table所有資料
    # Department.objects.all().delete()

    # 查詢department表格所有資料(QureySet資料)
    # data_list = Department.objects.all()
    # for data in data_list:
    #     print(data.depart_name, data.depart_menber)

    # 查詢department表格id=1的資料(QureySet資料)
    # data_id_1 = Department.objects.filter(id=1)
    # for data in data_id_1:
    #     print(data.depart_name, data.depart_menber)

    # 更新department表格id=2的資料
    # Department.objects.filter(id=2).update(depart_name='HR2',depart_menber=4)


    return HttpResponse('ORM create table success')

def orm_info_list(request):

    data_list = Department.objects.all()
    print(data_list)

    return render(request, 'orm_info_list.html', {'data_list': data_list})

def orm_user_info_list(request):

    data_list = UserInfo.objects.all()

    return render(request, 'orm_user_info_list.html', {'data_list': data_list})

def orm_user_add(request):
    if request.method == 'GET':
        return render(request, 'orm_user_add.html')
    
    user_name = request.POST.get('user_name')
    user_password = request.POST.get('user_password')
    user_age = request.POST.get('user_age')

    UserInfo.objects.create(name=user_name, password=user_password, age=user_age)

    return redirect('/orm/user_info_list')

def orm_user_delete(request):
    user_id = request.GET.get('user_id')

    UserInfo.objects.filter(id=user_id).delete()

    return redirect('orm_user_info_list')