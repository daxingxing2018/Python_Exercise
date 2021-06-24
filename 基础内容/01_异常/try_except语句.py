print('通过一个try对应一个except子句来达到捕捉多个异常')
def model_exception(x,y):
    try:
        b=name
        a=x/y
    except(ZeroDivisionError,NameError,TypeError):
        print('one of ZeroDivisionError or NameError or TypeError happened')
model_exception(2,0)
print('————————————————————————————————————————————————————————')

print('通过在一个try语句中添加多个except子句来达到捕捉多个异常')
def mult_exception(x, y):
    try:
        a = x / y
        b = name
    except ZeroDivisionError:
        print('this is ZeroDivisionError')
    except NameError:
        print('this is NameError')
mult_exception(2, 0)
print('————————————————————————————————————————————————————————')

print('添加as e来捕捉对象')
def model_exception(x, y):
    try:
        b = name
        a = x / y
    except(ZeroDivisionError, NameError, TypeError)as e:
        print(e)
model_exception(2, 0)
print('————————————————————————————————————————————————————————')

print('全捕捉')
def model_exception(x, y):
    try:
        b = name
        a = x / y
    except(ZeroDivisionError, NameError, TypeError)as e:
        print(e)
model_exception(2,'')