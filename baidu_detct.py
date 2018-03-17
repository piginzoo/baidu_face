# encoding:utf-8
import urllib, urllib2, sys
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
人脸探测
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v1/detect"


# 二进制方式打开图片文件
f = open('test2.jpg', 'rb')
img = base64.b64encode(f.read())

params = {
	"face_fields":"age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities",
	"image":img,
	"max_face_num":2}
params = urllib.urlencode(params)

request_url = request_url + "?access_token=" + access_token
request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print content

print "==================================="
result_dict = json.loads(content)
print result_dict['result']
print "==================================="
face_point = result_dict['result'][0]['landmark72']
for one in face_point:
	print "x=",one['x'],",y=",one['y']


import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
_face = pygame.image.load('test2.jpg')
screen.blit(_face,[0,0])
pygame.display.flip()

for one in face_point:
	x = one['x']
	y = one['y']
	# screen.set_at([x,y],[255,0,0])
	pygame.draw.circle(screen,[255,0,0],[x,y],2,0)
	pygame.display.flip()
while True:
	for e in pygame.event.get():
		if e.type== pygame.QUIT: sys.exit()
