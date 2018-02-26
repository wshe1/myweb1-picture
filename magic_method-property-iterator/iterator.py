#coding:utf-8
from collections import Iterator
class Fibs:#自定义胡迭代器
    def __init__(self):
        self.a=0
        self.b=1
    def next(self):
        self.a=self.b
        self.b=self.a+self.b
        return self.a
    def __iter__(self):
        return self


def func():
    print 'first'
    yield 1
    print 'second'
    yield 2
    print 'third'
    yield 3
    print 'fourth'

if __name__=='__main__':
    fibs=Fibs()
    f=fibs.next()
    print 1,f
    # for f in fibs:
    #     if f>1000:
    #         print 2,f
    #         break
    li=[1,2]
    it=iter(li)
    print 3,it
    print 4,it.next()#通过next()访问list中的元素，当访问完后抛出一个异常
    print 5,it.next()
    #print 6,it.next()
    g=func()
    print 7,g
    # print 8,isinstance(g,Iterator)#判断g是否是迭代器对象
    # print 9,next(g)
    # print 10,next(g)
    # print 11,next(g)
    i=iter(g)  #得到一个生成器
    print 12,i
    for i in g:#遍历生成器
        print i


