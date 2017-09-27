#!/usr/bin/env python
#-*-coding:utf-8-*-

'''import urllib.request
import urllib.parse

url = 'http://www.iqianyue.com/mypost/'
postdata = urllib.parse.urlencode({'name':'1234567@qq.com','pass':'654321'}).encode('utf-8')
req = urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3453.400 QQBrowser/9.6.12025.400')
data = urllib.request.urlopen(req).read()
fhandle=open('D:/6.html','wb')
fhandle.write(data)
fhandle.close()'''

#模拟如何登陆网页，就会发现成功的实现了post请求，并且完成了网页的爬取。


'''def use_proxy(proxy_addr,url):
    import urllib.request
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data
proxy_addr = '122.72.32.74:80'
data = use_proxy(proxy_addr,'http://www.baidu.com')
print(len(data))'''



'''import urllib.request
httphd = urllib.request.HTTPHandler(debuglevel=1)
httpshd= urllib.request.HTTPSHandler(debuglevel=1)
opener = urllib.request.build_opener(httphd,httpshd)
urllib.request.install_opener(opener)
data = urllib.request.urlopen('http://www.baidu.com')'''


import urllib.request
import urllib.error
try:
    urllib.request.urlopen('http://blog.baidusss.net')
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:
    print(e.reason)













