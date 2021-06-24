# 继承场景的多态
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 非继承场景的多态
class Duck(object):                                  # 鸭子类
    def fly(self):
        print("鸭子沿着地面飞起来了")
class Swan(object):                                  # 天鹅类
    def fly(self):
        print("天鹅在空中翱翔")
class Plane(object):                                 # 飞机类
    def fly(self):
        print("飞机隆隆地起飞了")

def fly(obj):                                        # 实现飞的功能函数
    obj.fly()

duck = Duck()
fly(duck)
swan = Swan()
fly(swan)
plane = Plane()
fly(plane)
