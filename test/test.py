#coding:utf-8
#当python 不捕识别汉字所以加上面一行
import logging
def demo_string():
    stra='hellO world';
    print stra.capitalize()#
    print stra.replace('world','shenghe')
    strb='   \n\rhello world \r\n'
    print strb
    print 1,strb.lstrip()
    print 2,strb.rstrip()
    strc='hello w'
    print 3,strc.startswith('hel')
    print 4,strc.endswith('x')
    print 5,strc.endswith('w')
    print 6,stra+strb+strc;
    print 7,len(strb)
    print 8,'-'.join(['a','b','c'])
    print 9,strc.split(' ')
    print 10,strb.find('hello')

def demo_operation():
    print 1,1+2,2/5,5*2
    print 2,True,not True
    print 3,1<2,4>2
    print 4,2<<3
    print 5,5|3,5&3,5^3
    x=3
    y=3.33
    print x,y,type(x),type(y)

def demo_buildfunction():
    print 1,max(3,2),min(3,2)
    print 2,len('ssdf'),len([1,2,3])
    print 3,abs(-2)
    print 4,range(1,10,3)
    print 5,dir(list)
    x=2
    print 6,eval('x+3')
    print 7,chr(97),ord('a')
    print 8,divmod(11,3)

def demo_controlflow():
    score=65
    if score>90:
        print 1,'A'
    elif score>60:
        print 2,'B'
    else:
        print 3, 'C'
    while score<100:
        print score
        score+=score
    score=65
    for i in range(0,10,2):
        if i==0:
            pass
        if i<5:
            continue
        print 4,i
        if i==6:
            break
def demo_list():
    lista=[1,2,3]#vector Arraylist
    print 1,lista
    listb=['a',1,'c']
    print  2,listb
    lista.extend(lista)
    print 3,lista
    print 4,len(lista)
    print 5,'a' in listb
    lista=lista+listb
    print 6,lista
    listb.insert(0,'www')
    print 7,listb
    listb.pop(1)
    print 8, listb
    listb.reverse();
    print 9, listb
    print 10,listb[0],listb[1]
    listb.sort()
    print 10, listb
    listb.sort(reverse=True)
    print 12, listb
    print 13,listb*2
    print 14,[0]*14#memset(src,0,len)
    tuplea=(1,2,3)
    listaa=[1,2,3]
    listaa.append(4)
    listaa[1]=6
    print 15, listaa
    del listaa[1]
    print 16, listaa
    listaaa=list('perl')
    listaaa[2:]=list('ars')
    print 17, listaaa
    listaaa[1:1]=[2,3,4]
    print 18, listaaa
    listaaa[1:4]=[]
    print 19, listaaa
    print 20,listaaa.count(2)
    print 21,listaaa.index('p')
    print 22,listaaa.remove('r')
    listaaa.reverse()
    print 23, listaaa

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def demo_dict():
    dicta={4:16,1:1,2:4,3:9}
    print 1,dicta
    print 2,dicta.keys(),dicta.values()
    print 3,dicta.has_key(1),dicta.has_key('3')
    for key,value in dicta.items():
        print 'key-value:',key,value
    dictb={'+':add,'-':sub}
    print 4,dictb['+'](1,2)
    print 5,dictb.get('-')(15,3)
    b={}.fromkeys([5,25])
    print 6,b

def demo_set():
    seta=set((1,2,3))
    setb=set((2,3,4))
    print 1,seta
    #seta.add(4)
    print 2,seta
    print 3,seta.intersection(setb),seta & setb
    print 4,seta | setb,seta.union(setb)
    print 5,seta-setb
    print 6,len(seta)
    print 7,seta.add('x')
    print 8,seta

class User:
    type='USER' #静态的变量
    def __init__(self,name,uid): #初始化函数，以self开头
        self.name=name
        self.uid=uid

    def __repr__(self): #默认的打印函数
        return 'im'+self.name+' '+str(self.uid)
class Admin(User): #继承了USER
    type='ADMIN'
    def __init__(self,name,uid,group): #由于继承了User，所以调用Userd的初始化函数
        User.__init__(self,name,uid)
        self.group=group
    def __repr__(self): #重载了打印函数（多态性）
        return 'im'+self.name+' '+str(self.uid)+self.group

class Networkerror(RuntimeError):
    def __init__(self,arg):
        self.args=arg

def demo_exception():
    try:
        print 2/1
        #print 2/0  #检测到异常自动的抛出，下面的代码不执行了
        raise Networkerror('bad running')
        if type=='c':
            raise Exception('Rasise Error', 'NowCoder')  # 手工的抛出异常
    except Networkerror as e:
        print e.args
        #logging.warning("running warning")#输出到控制台
        #logging.error("running debug")
        #logging.basicConfig(filename='example.log',level=logging.DEBUG)#level记录的级别，写到文件中
        #logging.basicConfig(filename='example.log',filemode='w', level=logging.DEBUG)#覆盖写入
        logging.basicConfig(filename='example.log',filemode='w',format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.debug("debug")
        logging.warning("waring")
        logging.error("error")
        logging.info('info')

    except Exception as e:#e是由Exception类实例化的一个对象;
        print 'error',e
    finally:
        print 'clean up'#最终不管是否出错都执行





if __name__ == '__main__':
    user1=User('u1',1)
    print user1
    admin1=Admin('al',101,'g1')
    print admin1
    #demo_string()
    #demo_operation()
    #demo_controlflow()
    #demo_list()
    #demo_dict()
    #demo_set()
    demo_exception()