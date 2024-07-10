from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class AuthMiddleware(MiddlewareMixin):
    
    def process_request(self, request):

        # 當使用者在登入頁面或註冊頁面時，不進行驗證
        if request.path_info == '/login/' or request.path_info == '/admin_account/':
            return None
        
        # 當使用者在登入狀態時，不進行驗證
        session_info = request.session.get('info')
        print(session_info)
        if session_info:
            return

        # 當使用者不在登入狀態時，導向登入頁面
        return redirect('/login/')

    # def process_response(self, request, response):

    #     print('AuthMiddleware process_response OUT')
    #     return response