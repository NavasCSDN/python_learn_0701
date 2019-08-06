import hashlib
import json
import time

import jwt
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from user.models import UserProfile


def btoken(request):

    if request.method != 'POST':
        result = {'code':101,'error':'Please use POST'}
        return JsonResponse(result)

    json_str = request.body
    if not json_str:
        #post 未提交 数据
        result = {'code': 102, 'error':'Please Post data'}
        return JsonResponse(result)

    json_obj = json.loads(json_str)
    username =json_obj.get('username')
    password =json_obj.get('password')

    if not username:
        result = {'code':103,'error':'Please give me username'}
        return JsonResponse(result)
    if not password:
        result = {'code': 104, 'error': 'Please give me password'}
        return JsonResponse(result)

    users = UserProfile.objects.filter(username=username)
    if not users:
        result = {'code':105,'error':'The user is not existed'}
        return JsonResponse(result)

    p_m = hashlib.sha1()
    p_m.update(password.encode())

    if p_m.hexdigest() != users[0].password:
        result = {'code':106, 'error':'The username or password is wrong'}
        return JsonResponse(result)


    # 生成token
    token = make_token(username)
    result = {'code':200, 'username':username,'data':{'token':token.decode()}}
    return JsonResponse(result)


def make_token(username, expire=3600 * 4):

    key = 'abcdef1234'
    now_t = time.time()
    payload = {'username': username, 'exp': int(now_t + expire)}
    return jwt.encode(payload, key, algorithm='HS256')