#-*- encoding=utf-8 -*-
'''
Created on 2016年9月30日

@author: Administrator
'''
#list切片
L = range(1, 101)
# print L[:10]
# print L[2::3]
# print L[4:50:5]


d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
values = d.values();
keys = d.keys();
# print keys
# print values

#列表生成式， 1*2 , 3*4 ,5*6 .... 99*100
print [x * (x + 1) for x in range(1,100,2)]


d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60 : 
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    else :
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

#请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
def toUppers(L):
    return [ x.upper() for x in L if isinstance(x,str) ]
print toUppers(['Hello', 'world', 101])


print [ x * 100 + y * 10 + z for x in range(1,10) for y in range(0,10) for z in range(0, 10) if x == z ]
