#coding:utf-8
#super用于调用父类，并返回父亲实例的方法
#supper:会找到第一个多继承中父类，如果调用其他父类的init()和两个父类的同名函数时就用老办法
class FooParent1(object):
    def __init__(self):
        self.parent1='I am the parent1'
        print 'parint1'

    def bar(self,message):
        print message+' from Parent1.'


class FooParent2(object):
    def __init__(self):
        self.parent2 = 'I am the parent2'
        print 'parint2'

    def bar(self, message):
        print message + ' from Parent2.'


class FooChild(FooParent1,FooParent2):
    def __init__(self):
        super(FooChild,self).__init__()
        FooParent2.__init__(self)
        print 'Child'

    def bar(self, message):
        super(FooChild,self).bar(message)
        FooParent2.bar(self,message)
        print 'Child bar function'
        print self.parent1
        print self.parent2

if __name__=='__main__':
    foochild=FooChild()
    foochild.bar('hello world')