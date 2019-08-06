# -*- coding:utf-8 -*-
 ######################################################
#        > File Name: flask_client.py
#      > Author: GuoXiaoNao
 #     > Mail: 250919354@qq.com 
 #     > Created Time: Mon 20 May 2019 11:52:00 AM CST
 ######################################################
'/usr/bin/python3'

from flask import Flask, send_file
#flask 默认静态文件目录[CSS, JS, IMG]在static
#flash 默认模板目录在templates



#初始化Flask
app = Flask(__name__)

#修饰器绑定路由URL
@app.route('/index')
def index():
    #首页
    #sendfile  直接返回具体的页面
    return send_file('templates/index.html')

@app.route('/login')
def login():
    #登录
    return send_file('templates/login.html')

@app.route('/register')
def register():
    #注册
    return send_file('templates/register.html')

@app.route('/<username>/info')
def info(username):
    #个人信息
    return send_file('templates/about.html')

@app.route('/<username>/change_info')
def change_info(username):
    #修改个人信息
    return send_file('templates/change_info.html')

@app.route('/<username>/topic/release')
def topic_release(username):
    #发表博客
    return send_file('templates/release.html')


@app.route('/<username>/topics')
def topics(username):
    #个人博客列表
    return send_file('templates/list.html')

@app.route('/<username>/topics/detail/<t_id>')
def topics_detail(username, t_id):
    #博客内容详情
    return send_file('templates/detail.html')

@app.route('/test')
def test():
    return send_file('templates/test.html')

if __name__ == '__main__':
    #启动flash服务，debug参数-True则进入调试模式
    #linux 命令行中，执行python3 当前文件名，即可开启服务
    #默认监听5000
    app.run(debug=True)

