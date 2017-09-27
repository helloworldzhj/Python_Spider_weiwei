#!/usr/bin/env python
#-*-coding:utf-8-*-

'''import re
pattern = 'yue'
string = 'http://yum.iqianyue.com'
result=re.search(pattern,string)
print(result)'''

'''import re
pattern = '\n'
string = 'http://yum.iqianyue.com
         http://baidu.com'
#这边要使用三引号
result1=re.search(pattern,string)
print(result1)'''


'''import re
string = 'apythonhellomypythonhispythonourpythonend'
pattern = '.python.'
result=re.match(pattern,string)
result2 = re.match(pattern,string).span()
print(result)
print(result2)
#这样只能匹配到第一个结果，其他的不显示，下面的例子显示'''

'''import re
string = 'apythonhellomypythonhispythonourpythonend'
pattern = re.compile('.python.')
result=pattern.findall(string)
print(result)
#通过re.compile()对正则表达式进行预编译，编译后使用findall（）根据正则表达式从源字符串中将匹配的结果全部找出'''

'''import re
string = 'apythonhellomypythonhispythonourpythonend'
pattern = '.python.'
result=re.compile(pattern).findall(string)
print(result)
#将前面两个句子整合起来，就成了现在的这个更短的py'''








