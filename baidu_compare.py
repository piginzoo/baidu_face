# encoding:utf-8
import urllib, urllib2, sys,os
import ssl
import base64
import urllib
import urllib2
import json

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=EL8U4aKIOXGHceWO4doLQs50&client_secret=y55tW4FAohCnLlGVhdm2eWVF9sGI6xMW'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
at = response.read()
print at
dict = json.loads(at)
access_token =  dict['access_token']

'''
人脸对比
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v2/match"

f = open('test1.jpg', 'rb')
# 参数images：图像base64编码
img1 = base64.b64encode(f.read())
# 二进制方式打开图文件
f = open('test5.jpg', 'rb')
# 参数images：图像base64编码
img2 = base64.b64encode(f.read())

params = {"images":img1 + ',' + img2}
params = urllib.urlencode(params)

# access_token = '[调用鉴权接口获取的token]'
request_url = request_url + "?access_token=" + access_token
request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print content
result = json.loads(content)
score = result['result'][0]['score']
if score>80:
	os.system("say 偶的神啊，你们长得跟孪生兄弟一样呀，太太太太太太太太像了！")
else:
	os.system("say 你们两个是不一样的，六耳猕猴，快现出你的原型吧，哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈")