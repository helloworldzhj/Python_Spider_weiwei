#!/usr/bin/env python
#-*-coding:utf-8-*-

# 实例1：匹配url网址

'''import re
pattern = '[a-zA-Z]+://[^\s]*[.com|.cn]'
string = "<a href='http://www.baidu.com'>百度首页</a>"
result = re.search(pattern,string)
print(result)'''

#在这个例子中，关键点在于正则表达式的设置，要构建好相对完善的正则表达式，需要我们观察我们需求的这些信息的规律。首先‘：//’是固定的，可以写出来。然后我们要以。com|。cn结尾，所以正则表达式的最后要以[.com\.cn]结尾。而且在这二者之间不能出现空格所以我们可以写为[^\s]*,在‘：//’之前必须要有内容，所以必须要有一次重复，故而我们用+而不用*号，这些内容可以是任意的字符的组合，包括大小写，所以可用[a-zA-Z]组合起来所以得到了上面的正则表达式

#实例2：匹配电话号码

'''import re
pattern = '\d{4}-\d{7}|\d{3}-\d{8}'
string = '021-2461846821382138246124361853'
result=re.search(pattern,string)
print(result)'''
#这个正则表达式的话稍微简单了点，就这样吧


#实例3

import re
pattern = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"
string = "<a href='http://www.baidu.com'>百度首页</a><br><a href='mailto:c-e+o@iqianyue.com.cn'>电子邮件地址</a>"
result=re.search(pattern,string)
print(result)

#在本例中，关键点还是在于正则表达式的设置，要设置好匹配电子邮件的正则表达式，则需要观察电子邮件的格式，然后总结出一套模式出来。简单提示一下，首先确定电子邮件的@符号，然后观察@后可以出现哪些字符，@前可以出现哪些字符，并通过正则表达式描述出来。设置好正则表达式以后，同样可以通过re。search函数将符合条件的信息匹配提取出来。






























