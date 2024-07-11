from django.conf import settings
import hashlib

def md5(data_string):
    # 建立md5物件
    object = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    # 更新md
    object.update(data_string.encode('utf-8'))
    # 回傳md5加密後的字串
    return object.hexdigest()