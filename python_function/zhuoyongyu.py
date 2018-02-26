#coding:utf-8
import __builtin__
#函数内的解释规则：（1）：先是在函数内部的本地作用域（本地函数是def ,lambda,定义的），2）然后是上一层的函数本地作用域（多层嵌套函数）
#3）然后是全局作用域，（在模块的顶层赋值胡变量名，或则，函数内部使用global）4）最后是内置作用域（python在运行之前会自动的引用一个内置的模块__builtin__)。
def func():
    #x=10#局部变量作作用域是本函数内
    global x#声明了一个全局变量
    print 'insde func:x is{}'.format(x)
    x=10
    print 'chang x:{}'.format(x)

def printmessage(message,times):
    print message*times

def printmessage1(message,times=3):#默认参数必须放在最右边
    print message*times
def func1(a,b=10,c=20):
    print 'a is:',a,'b is :',b,'c is :',c

def printScore(msg,*values):
    if not values:
        print msg
    else:
        values_str=','.join(str(x)for x in values)
        print '{},{}'.format(msg,values_str)

def printlog(msg,**therest):#使用**来表示
    if not therest:
        print msg
    else:
        for key,value in therest.items():
            print('{},{}={}'.format(msg,key,value))

def toal(inital=5,*numbers,**keywords):
    count=inital
    for number in numbers:
        count+=number

    for key in keywords:
        count+=keywords.get(key)
    return count
if __name__=='__main__':
    x=100#x是全局变量作用域是整个
    func()
    print 1,'x still is{}'.format(x)
    print 2,dir(__builtin__)
    #位置参数：所有参数在传递时按照位置来传递
    printmessage('hello world ',2)
    #默认参数传递
    printmessage1('hello world ')
    #关键参数传递,是通过变量名进行匹配的
    func1(3,7)
    func1(25,c=24)
    func1(b=50,a=25)
    #任意数量的参数
    printScore('my score is:')
    printScore('myscore is:',20,30,40,50)
    #任意多个关键字的形式参数，
    printlog('Log info',version='01',platfrom='win7')
    #综合的例子
    print toal(10,1,2,3,4,apple=50,orgne=100)




