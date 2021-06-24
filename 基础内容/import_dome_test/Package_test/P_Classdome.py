class package():
    def Foo(self):
        print("hello world")

class two():
    def Foo2(self):
        print("hello Python")

def use_finally(x, y):
    try:
        a = x / y
    except ZeroDivisionError:
        print('Some bad thing happened:division by zero')
    finally:
        print('No matter what happened,l will show in front of you')