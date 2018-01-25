#coding:utf-8
#用于判断对象是否包含对应的属性
#hsaattr(object,name);object -对象;name--字符串，属性名
class test1:
    def __init__(self):
        self.x=3
        self.y=6

if __name__=='__main__':
    a=test1()
    print 1,hasattr(a,'x')
    print 2,hasattr(a,'y')
    print 3,hasattr(a,'z')