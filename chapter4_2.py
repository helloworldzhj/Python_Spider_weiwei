#!/usr/bin/env python
#-*-coding:utf-8-*-

'''import urllib.request
keyword = str(input('你想搜索什么：'))
#首先定义要查询的关键词，并赋给keywd变量
url = 'http://www.baidu.com/s?wd='+keyword
#按照分析出来的url格式构造对应的url并赋值给url变量
req = urllib.request.Request(url)
#随后使用urllib.request.Request()构建一个request对象并赋值给变量req
data = urllib.request.urlopen(req).read()
#通过urllib.request.urlopen()打开对应的request对象，此时由于网址中包含了get请求信息，所以会以get请求的方式获取该页面，随后读取该页面的内容并赋值给变量data
fhandle= open('D:/4.html','wb')
#再将爬取到的内容写入文件
fhandle.write(data)
fhandle.close'''

#这段代码又有点错误，当输入为中文时，会出现编码问题


import urllib.request
key = '微微老师'
url = 'http://www.baidu.com/s?wd='
key_code=urllib.request.quote(key)
url_all=url+key_code
req = urllib.request.Request(url_all)
data = urllib.request.urlopen(req).read()
fh= open('D:/5.html','wb')
fh.write(data)
fh.close

#构建对应的url地址
#以对应的url为参数 构建request对象
#通过urlopen打开构建的request对象
#按需求进行后续的处理操作，比如读取网页的内容，将内容写入文件

















