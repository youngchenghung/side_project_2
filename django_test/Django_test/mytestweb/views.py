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

from mytestweb import models

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

def orm_department_info_list(request):

    data_list = models.Department.objects.all()
    print(data_list)

    return render(request, 'orm_department_info_list.html', {'data_list': data_list})

def orm_department_add(request):
    if request.method == 'GET':
        return render(request, 'orm_department_add.html')

    depart_name = request.POST.get('depart_name')
    depart_member = request.POST.get('depart_member')

    models.Department.objects.create(depart_name=depart_name, depart_member=depart_member)

    return redirect('orm_department_info_list')

def orm_department_edit(request, nid):
    if request.method == 'GET':
        depart_name = models.Department.objects.get(id=nid).depart_name
        depart_member = models.Department.objects.get(id=nid).depart_member
        return render(request, 'orm_department_edit.html', {'depart_name': depart_name, 'depart_member': depart_member})


    depart_name = request.POST.get('depart_name')
    depart_member = request.POST.get('depart_member')
    models.Department.objects.filter(id=nid).update(depart_name=depart_name, depart_member=depart_member)

    return redirect('orm_department_info_list')

def orm_department_delete(request):
    
    depart_id = request.GET.get('depart_id')

    models.Department.objects.filter(id=depart_id).delete()

    return redirect('orm_department_info_list')

def orm_user_info_list(request):

    data_list = models.UserInfo.objects.all()

    return render(request, 'orm_user_info_list.html', {'data_list': data_list})

def orm_user_add(request):
    if request.method == 'GET':

        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all()
            }

        return render(request, 'orm_user_add.html', context)
    
    name = request.POST.get('user_name')
    password = request.POST.get('user_password')
    age = request.POST.get('user_age')
    account = request.POST.get('user_account')
    create_time = request.POST.get('user_create_time')
    gender = request.POST.get('user_gender')
    depart_foreignkey_id = request.POST.get('id')

    models.UserInfo.objects.create(name=name, 
                                   password=password, 
                                   age=age, account=account, 
                                   create_time=create_time, 
                                   gender=gender, 
                                   depart_foreignkey_id=depart_foreignkey_id
                                   )

    return redirect('/orm/user_info_list')

def orm_user_delete(request):
    
    user_id = request.GET.get('user_id')

    models.UserInfo.objects.filter(id=user_id).delete()

    return redirect('orm_user_info_list')

from django import forms
from mytestweb.module.encrypt_md5 import md5

# 建立類別ModelFormUserInfo，繼承forms.ModelForm
class ModelFormUserInfo(forms.ModelForm):
    name = forms.CharField(min_length=1, label='Name')
    password = forms.CharField(min_length=8, label='Password')

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart_foreignkey']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', "placeholder": field.label}

# 建立modelform_add_user函數
def modelform_add_user(request):
    if request.method == 'GET':
        form = ModelFormUserInfo()
        return render(request, 'modelform_add_user.html', {'form': form})

    # 將request.POST資料傳入ModelFormUserInfo
    form = ModelFormUserInfo(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/orm/user_info_list')

    return render(request, 'modelform_add_user.html', {'form': form})

# 建立modelform_user_edit函數
def modelform_user_edit(request, nid):
    if request.method == 'GET':

        # 取得資料庫中指定id的欄位資料
        row_object = models.UserInfo.objects.filter(id=nid).first()

        # 代入instance參數到ModelFormUserInfo
        form = ModelFormUserInfo(instance=row_object)
        return render(request, 'modelform_user_edit.html', {'form': form})
    
    # 取得資料庫中指定id的欄位資料
    row_object = models.UserInfo.objects.filter(id=nid).first()
    
    # 將request.POST資料傳入ModelFormUserInfo
    # 代入instance參數到ModelFormUserInfo
    form = ModelFormUserInfo(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/orm/user_info_list')
    
    return render(request, 'modelform_user_edit.html', {'form': form})


    
# 建立類別ModelFormAdminAccount，繼承forms.ModelForm
class ModelFormAdminAccount(forms.ModelForm):
    
    class Meta:
        model = models.AdminAccount
        fields = ['admin_name', 'admin_password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', "placeholder": field.label}

    # 針對password欄位進行MD5加密
    def clean_admin_password(self):
        admin_password = self.cleaned_data.get('admin_password')
        return md5(admin_password)
    
# 建立admin_account函數
def admin_account(request):
    if request.method == 'GET':
        form = ModelFormAdminAccount()

        return render(request, 'orm_admin_account.html', {'form': form})
    
    # 將request.POST資料傳入ModelFormAdminAccount
    form = ModelFormAdminAccount(data=request.POST)
    # 驗證表單是否正確
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        return redirect('/login/')

# 建立login函數
def login(request):
    if request.method == 'GET':
        form = ModelFormAdminAccount()

        return render(request, 'orm_login.html', {'form': form})
    
    # 將request.POST資料傳入ModelFormAdminAccount
    form = ModelFormAdminAccount(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)

        # 查詢資料庫中是否有符合的資料
        check_account = models.AdminAccount.objects.filter(**form.cleaned_data).first()
        # 如果沒有符合的資料，則顯示錯誤訊息
        if not check_account:
            form.add_error("admin_password", 'Account and Password is incorrect')
            return render(request, 'orm_login.html', {'form': form})
        
        # 如果有符合的資料，則將admin_name存入session
        request.session['info'] = {'admin_name': form.cleaned_data['admin_name']}
        
    return redirect('/orm/user_info_list')
    