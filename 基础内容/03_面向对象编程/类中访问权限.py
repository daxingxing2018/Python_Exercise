'''
# 在类外修改了类的属性
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def info(self):
        print('学生：%s; 分数：%s'%(self.name,self.score))
stu = Student('Xiaoming',99)
print('修改前的分数：',stu.score)
stu.info()
stu.score=0
print('修改后的分数：',stu.score)
stu.info()
'''

'''
# 将类的属性设置成了不可访问状态
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def info(self):
        print('学生：%s; 分数：%s'%(self.__name,self.__score))
stu = Student('Xiaoming',99)
print('修改前的分数：',stu.__score)   # 这行开始就会报错，因为访问了没有权限的类属性
stu.info()
stu.__score=0
print('修改后的分数：',stu.__score)
stu.info()
'''
# 访问私有属性和更改私有属性的方法
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def info(self):
        print('学生：%s; 分数：%s'%(self.__name,self.__score))

    def get_score(self):
        return self.__score
'''
    def set_score(self,score):
        self.__score = score
'''
    if 0<=score<=100:
        self.__score = score
    else:
        print('请输入0到100之间的数字')
stu = Student('Xiaoming',99)
print('修改前的分数：',stu.get_score())
stu.info()
stu.set_score(-10)
print('修改后的分数：',stu.get_score())
stu.info()


# 私有方法的使用
class PrivatePublicMethod(object):
    def __init__(self):
        pass
    def __foo(self):      # 私有方法
        print('这是一个私有方法')
    def foo(self):        # 公共方法
        print('这是公共方法')
        print('公共方法中调用私有方法')
        self.__foo()
        print('公共方法中调用私有方法结束')

pri_pub = PrivatePublicMethod()  # 实例化这个类
print("开始调用公共方法")
pri_pub.foo()
print("开始调用私有方法")
pri_pub.__foo()
