#!/usr/bin/env python
#coding:utf-8

'''源码仅用于学习交流，请勿非法使用！'''

import requests
import getpass
import re

def login(user, password):
    '''模拟登录请求，成功返回cookiesjar类型，否则返回空'''
    loginPostURL = 'http://home.51cto.com/index.php?s=/Index/doLogin'
    loginHeaders = {'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0'}
    postData = {'email' : user,
                'passwd' : password,
                'authlogin' : 'on'}
    loginSession = requests.Session()
    loginSession.headers = loginHeaders
    loginRequest = loginSession.post(loginPostURL, data = postData)
    if re.match(r'^<script', loginRequest.text):
        print '登录成功！'
        print '获取cookies中……'
        pattern = re.compile(r'src="(http://\w+?\.51cto\.com.+?)"')
        for apiURL in pattern.findall(loginRequest.text):
            apiURLRequest = loginSession.get(apiURL)
        print '获取cookies完毕'
        return loginSession.cookies
    else:
        print '登录失败！'
    loginSession.close()

def requestEdu(cj):
    '''模拟edu.51cto.com登录'''
    eduURL = 'http://edu.51cto.com/'
    requestHeaders = {'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0'}
    requestSession = requests.Session()
    requestSession.cookies = cj
    requestSession.headers = requestHeaders
    request = requestSession.get(eduURL)
    with open('edu51cto.html', 'w') as f:
        f.write(request.text.encode('utf-8'))


def main():
    user = raw_input('user: ')
    password = getpass.getpass('password: ')
    cj = login(user, password)
    if cj:
        requestEdu(cj)

if __name__ == '__main__':
    main()
