#coding:utf-8
from functools import partial
import functools

def log(func):# 传入的是函数指针
    def wrapper():#内嵌函数
        print 'before calling',func.__name__
        func()
        print 'end calling ',func.__name__
    return wrapper
#*无名参数
#**有名参数
def log1(func):# 传入的是函数指针
    def wrapper(*args,**kvargs):#内嵌函数
        print 'before calling',func.__name__
        print 'args',args,'kvargs',kvargs
        func(*args,**kvargs)
        print 'end calling ',func.__name__
    return wrapper

@log
def hello():
    print 'hello'
@log1
def hello2(name,age):
    print 'hello',name,age
def log2(level,*args,**kvargs):# 传入的是函数指针
    def inner(func):
        def wrapper(*args,**kvargs):#内嵌函数
            print level,'before calling',func.__name__
            print level,'args',args,'kvargs',kvargs
            func(*args,**kvargs)
            print level,'end calling ',func.__name__
        return wrapper
    return inner

@log2(level='INFO')
def hello3(name,age):
    print 'hello',name,age

def hello1():
    hello1.name = 'wshe'#定义函数属性

    print 'hello world'
    hello1.__dict__['age']=24#定义函数属性

n=lambda x,y:x*y #匿名函数


if __name__=='__main__':
    hello()#log(hello)
    hello1()
    print 1,hello1.__dict__ #__dict__ 获得所有函数胡属性名和属性值
    #显示函数的属性和属性值
    print 2,type(n(2,3))#调用匿名函数
    print 3,n(2,3)
    int2=functools.partial(int,base=2)
    print 4,int2('1010')#输入的是2进制
    print 5,int2('1010',base=10) #输入胡是十进制
    print 6,hello2('wshe',25) #调用的是无名参数
    print 7,hello2(name='wshe',age=5)#调用的是有名参数
    print 8,hello3(name='wshe',age=6)#设置不同水平