#coding:utf-8
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.instance=add
        self.instance1=sub
    #分别调用不太的方法
    def __call__(self, *args, **kwargs):
        for key in kwargs:#获取有名参数的方法
            typesa=kwargs[key]
        if typesa=='1':
            return self.instance(*args)
        else:
           return self.instance1(*args)

    #这样写,同时调用两个方法
    # def __call__(self, *args, **kwargs):
    #     return self.instance(*args),self.instance1(*args)

    #__new__ methods
    # def __new__(cls, *args, **kwargs):
    #     #每一次实例化，都只会返回同一个instt对象
    #     if not hasattr(cls,'name'):
    #         cls.instt=super(Person,cls).__new__(cls)
    #     print 1,cls.instt
    #     return cls.instt

def add(args):
    return args[0]+args[1]
def sub(args):
    return args[0]*args[1]

if __name__=='__main__':
    a=Person('instt',20)
    print a.name,a.age
    b=Person('p2',21)
    print 1,(a==b)
    print 2,a.name,a.age,b.name,b.age
    print 3,a([1,2],types='1')
    print 4,a([2,3],types='0')