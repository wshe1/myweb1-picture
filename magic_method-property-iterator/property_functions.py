#coding:utf-8
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # def semth():#静态方法
    #     print 'This is a static method'
    # semth=staticmethod(semth)
    #
    # def cmeth(cls):#类方法
    #     print 'This is a class method of',cls
    # cmeth=classmethod(cmeth)
    @staticmethod #装饰器版的静态方法
    def semth():
        print 'This is a static method 1'

    @classmethod#装饰器版的类方法
    def cmeth(cls):
        print 'This is a class method1 of', cls

    def setSex(self,name_age):#这里的变量是调用地属性的名字，是一个tuple
        self.name=name_age[0]
        self.age=name_age[1]

    def getSex(self):
        return self.name,self.age

    def delSex(self):
        del self.name,self.age

    name_age=property(getSex,setSex,delSex)#使用property函数，相当于提供了一个统一的接口，当函数名修改时用户不需要修改调用

if __name__=="__main__":
    a=Person('wshe','25')
    print 1,a.name,a.age
    print 2,a.name_age
    a.name_age='wang','25'
    print 3,a.name_age
   # del a.name_age
    #print 4,a.name_age
    print 5,a.semth()
    print 6,a.cmeth()