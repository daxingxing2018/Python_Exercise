class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def info(self):
        print('学生：%s; 分数：%s'%(self.name,self.score))

stu=Student('xiaoming',95)