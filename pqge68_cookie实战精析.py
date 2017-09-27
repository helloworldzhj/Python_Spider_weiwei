#!/usr/bin/env python
#-*-coding:utf-8-*-

'''import urllib.request
import urllib.parse

url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lxl7g'
postdata = urllib.parse.urlencode({
    'username':'子夜破晓',
    'password':'zhj3632402'
}).encode('utf-8')
req = urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3453.400 QQBrowser/9.6.12025.400')
data = urllib.request.urlopen(req).read()
fhandle = open('D:/1.html','wb')
fhandle.write(data)
fhandle.close()

url2='http://bbs.chinaunix.net/'
req2=urllib.request.Request(url2,postdata)
req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3453.400 QQBrowser/9.6.12025.400')
data2 = urllib.request.urlopen(req2).read()
fhandle = open('D:/2.html','wb')
fhandle.write(data2)
fhandle.close()'''

'''在这个代码中，设置好登陆网址和构建好数据后，使用urllib.request.Request()创建了一个Request对象，然后添加了对应的头文件，随后使用了urllib.request.urlopen()函数进行登陆并爬取了对应的网页信息保存到本地文件1.html中，然后再爬取该网站下其他网页并保存到本地文件2.html中。
但是这么做是有不到位的地方的第二个网页中仍然需要登录，因为没有设置cookie处理
那么如果需要登录状态一直存在，就需要cookie处理
进行cookie处理的一种常用思路如下：
1.导入cookie处理模块http.cookiejar
2.使用http。cookiejar。创建cookiejar对象
3.使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
4.创建全局默认的opener对象'''

#所以代码改进如下：

import urllib.request
import urllib.parse
import http.cookiejar

url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lxl7g'
postdata = urllib.parse.urlencode({
    'username':'子夜破晓',
    'password':'zhj3632402'
}).encode('utf-8')
req = urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3453.400 QQBrowser/9.6.12025.400')
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
file = opener.open(req)
data = file.read()
file=open('D:/3.html','wb')
file.write(data)
file.close()
url2='http://bbs.chinaunix.net/'
data2 = urllib.request.urlopen(url2).read()
fhandle = open('D:/4.html','wb')
fhandle.write(data2)
fhandle.write(data2)

#说起来又有点遗憾，这个我并没有实现，不过代码的话我觉得是没有问题的，主要是可能网页改版了，或者说我这个是网页自动跳转的。所以可能是这方面的问题。