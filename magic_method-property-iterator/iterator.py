#coding:utf-8
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

