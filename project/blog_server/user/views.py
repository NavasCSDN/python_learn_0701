import hashlib
import json
import time

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
import jwt

from btoken.views import make_token
from user.models import UserProfile


def users(request, username = None):

    if request.method == 'GET':
        all_users = UserProfile.objects.all()
        res = []
        for u in all_users:
            d = {}
            d['username'] = u.username
            d['email'] = u.email
            res.append(d)
        result = {'code':200, 'data':res}
        return JsonResponse(result)

    elif request.method == 'POST':

        json_str = request.body
        if not json_str:
            result = {'code':'202', 'error':'Please POST data'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        username = json_obj.get('username')
        email = json_obj.get('email')
        password_1 = json_obj.get('password_1')
        password_2 = json_obj.get('password_2')
        if not username:
            result = {'code':203, 'error':'Please give me uesrname'}
            return JsonResponse(result)
        if not email:
            result = {'code':204, 'error':'Please give me email'}
            return JsonResponse(result)
        if not password_1 or not password_2:
            result = {'code':205, 'error':'Please give me password'}
            return JsonResponse(result)

        if password_1 != password_2:
            result = {'code':206, 'error':'The password is wrong!'}
            return JsonResponse(result)
        #检查用户是否存在
        old_user = UserProfile.objects.filter(username = username)
        if old_user:
            result = {'code':207, 'error':'The username is existed!!!'}
            return JsonResponse(result)

        h_p = hashlib.sha1()
        h_p.update(password_1.encode())
        try:
            UserProfile.objects.create(username=username,nickname=username,email=email,
                                       password=h_p.hexdigest())
        except Exception as e:
            print('UserProfile create error is %s'%(e))
            result = {'code': 207, 'error': 'The username is existed!!!'}
            return JsonResponse(result)
        token = make_token(username)
        result = {'code':200, 'username':username,'data':{'token': token.decode()}}
        return JsonResponse(result)

    elif request.method == 'PUT':
        pass
        users  = UserProfile.objects.filter(username = username)
        if not users:
            result = {'code':208,'error':'The user is not existed'}
            return JsonResponse(result)

        json_str = request.body
        if not json_str:
            result = {'code':202,'error':'Please give me data'}
            return JsonResponse(result)

        json_obj = json.loads(json_str)
        nickname = json_obj.get('nickname')
        if not nickname:
            result = {'code':209, 'error':'nickname is none!'}
            return JsonResponse(result)
        sign = json_obj.get('sing','')
        info = json_obj.get('info','')

        users[0].sign = sign
        users[0].info = info
        users[0].nickname = nickname
        users[0].save()

        result = {'code':200, 'username':username}
        return JsonResponse(result)

    return JsonResponse({'code':200, 'data':{'username':1}})