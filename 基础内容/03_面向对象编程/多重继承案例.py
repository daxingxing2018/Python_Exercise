# 第一步
# 创建了Animal大类，类中的属性和方法可以先用pass跳过
class Animal(object):
    pass
# 第二步
# 创建了哺乳动物和鸟类，并且都继承了Animal大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass
# 第三步
# 创建行为能力类
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')

# 第四步
# 创建详细的动物，需要什么动物属性或者能力属性，直接继承就好了
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
class Parrot(Bird,Flyable):
    pass
class Ostrich(Bird,Runnable):
    pass
