#coding:utf-8
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.instance=add
        self.instance1=sub
        self._registry={
            'name':name,
            'age':age
        }

    #返回集合中所含项目的数来拿量

    def __len__(self):
        return len(self._registry)

    #用户定义用户试图访问一个不存在属性胡时候的行为
    def __getattr__(self, item):
        print("don't have the attribute ",item)
        return False

    def __setattr__(self, key, value):
        self.__dict__[key]=value

    def __getattribute__(self, item):
        return object.__getattribute__(self,item)

     #存储Key和相关的value
    def __setitem__(self, key, value):
        self._registry[key]=value

    #定义获取容中指定元素的行为，相当于self[key]
    def __getitem__(self, item):
        if item not in self._registry.keys():
            raise Exception('Please registry the key:%s first!' %(item,))
        return self._registry[item]
    #删除key 值
    def __delitem__(self, key):
        del self._registry[key]

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
bokeyuan={"b":1,"o":2,"k":3,"e":4,"y":5,"u":6,"a":7,"n":8,}#一个属性的字典，

class Dict2Obj:
    def __init__(self,bokeyuan):
        self.__dict__.update(bokeyuan)#dit中的update方法，代替给原来属性的赋值的结构，：dict[key]->value.

if __name__=='__main__':
    a=Person('instt',20)
    print a.name,a.age
    b=Person('p2',21)
    print 1,(a==b)
    print 2,a.name,a.age,b.name,b.age
    print 3,a([1,2],types='1')
    print 4,a([2,3],types='0')
    print 5,a['name'],a['age']
    print 6,a.hh#打印出错误
    a.hh='wshe'
    print 7,a.hh#打印出信息
    c=Dict2Obj(bokeyuan)
    print 8,c.__dict__
    print 9,a.__len__()
    a.__setitem__('sex','man')
    print 10,a['name'],a['age'],a['sex']
    print 11, a._registry
    a.__delitem__('sex')
    print 12,a._registry
