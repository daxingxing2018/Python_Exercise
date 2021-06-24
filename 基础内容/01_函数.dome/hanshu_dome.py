'''
# 关键字参数
def personinfo(age,name):
    print('年龄：',age)
    print('名称：',name)
    return
print('-----按照参数顺序传入参数-----')
personinfo(21,'小萌')
print('-----不按参数顺序传入参数，指定参数名-----')
personinfo(name='小萌',age=21)
print('-----按参数顺序传入参数，指定参数名-----')
personinfo(age=21,name='小萌')

# 默认参数
#def defaultparam(age=23,name):   默认参数age, 在必须参数name前面了，这样写会报错的
def defaultparam(name,age=23):
    print('hi,我叫：',name)
    print('我今年：',age)
    return
defaultparam('小萌')

# 可变参数
def personinfo(arg,*vartuple):
    print(arg)
    for var in vartuple:
        print("我属于不定长参数部分：",var)
    return
print('----不带可变参数-----')
personinfo('小萌')
print('----带两个可变参数-----')
personinfo('小萌',21,'beijing')
print('----带5个可变参数-----')
personinfo('小萌',21,'beijing',123,'happy')

# 组合参数
def exp(p1,p2,df=0,*vart,**kw):
    print('p1=',p1,'p2=',p2,'df=',df,'vart=',vart,'kw=',kw)
#exp(1,2)
#exp(1,2,c=3)
#exp(1,2,3,'a','b')
#exp(1,2,3,'abc',x=9)
args=(1,2,3,4)  #定义一个tuple
kw={'x':8,'y':'10'}  #定义一个dict
exp(*args,**kw)
'''

#
num = 100
print('函数调用前num的值为：',num)
def func():
    global num
    num = 200
    num += 100
    print('函数体中num的值为：',num)
func()
print('函数调用结束后 num 的值为：',num)



