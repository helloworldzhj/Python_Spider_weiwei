#!/usr/bin/env python
#-*-coding:utf-8-*-

'''import urllib.request
url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3453.400 QQBrowser/9.6.12025.400')
opener = urllib.request.build_opener()
opener.assheaders = [headers]
data = opener.open(url).read()
fhandle = open('D:/3.html','wb')
fhandle.write(data)
#print(fhandle.write(data))
fhandle.close()
#这边只是获得一个网页的很简单的全部信息，也没有什么其他的特殊内容'''

#方法1：使用build_opener()修改报头



'''import urllib.request
url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3453.400 QQBrowser/9.6.12025.400')
data = urllib.request.urlopen(req).read()
fhandle = open('D:/3.html','wb')
fhandle.write(data)
#print(fhandle.write(data))
fhandle.close()
#这边只是获得一个网页的很简单的全部信息，也没有什么其他的特殊内容'''

#方法2：使用add_header()添加报头


import urllib.request
for i in range(1,100):
    try:
        file = urllib.request.urlopen('http://yum.iqianyue.com',timeout=30)
        data = file.read()
        print(len(data))
    except Exception as e:
        print('出现异常-->'+str(e))

