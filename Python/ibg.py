# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:49:42 2019

@author: abhis
"""

a=6.3
b=2
#print(a//b)


a=lambda x:x*3
b=lambda x:x*2
y=3
y=a(y)
y=b(y)
y=a(y)
print(y)

a={'a':2,'b':1,'c':3}
del a['a']
a['a']=2
del a['c']
print(len(a))

x=123
y=0
#for i in x:
#    y+=i
print(y)

e={1:3}
v={3:4,4:5}
pair=(v.get(1),v[3])
print(pair)

en=(1,'two',3)
print([e for e in en if type(e)==str])

class IntWrap():
    def __init__(self,a):
        self.a=a
    
a={1:IntWrap(1)}
b={2:a[1]}
c={3:b[2]}
d=b[2]
e=c[3]

print(a,b,c,d,e)

class A(object):
    def foo1(self):
        print('foo1 called')
    def foo2(self):
        print('foo2 called')
        

ob=A()
A.foo1(ob)

print('abcdef89'.replace('de','89'))


l=[1,2,[3,4]]
l2=l.copy()
l2[0]=7
print(l)
print(l2)

l1=[(1,2),
    (3,4)]

print('Good moring {0} and {1}'.format('IBG','THI'))

x=['hi','gr']
x2=x[:]
x3=['g','gg']

x3[0]='thu'
x2[1]='ibg'

print(x)
print(x2)
print(x3)

for c in (x,x2,x3):
    pass
    #print(c[0])
    #print(c[1])

    