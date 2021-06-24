'''
# 返回函数
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3=count()
print('f1执行的结果是：',f1())
print('f2执行的结果是：',f2())
print('f3执行的结果是：',f3())
f4=count()
print('f4执行的结果是：',f4)

# 能正常使用循环变量的返回函数
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))  # f(i) 立刻被执行，因此 i 的当前值被传入 f()
    return fs

f1,f2,f3=count()
print('f1执行的结果是：',f1())
print('f2执行的结果是：',f2())
print('f3执行的结果是：',f3())

# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
print('调用递归函数执行结果为：',fact(5))

# 尾递归函数
def fact1(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)
print('调用递归函数执行结果为：',fact1(5))

# 正常函数求一个列表中大于3的值
def func(x):
    return x>3
f_list=filter(func,[1,2,3,4,5])
print('列表中大于3的元素有：',[item for item in f_list])

# 匿名函数求一个列表中大于3的值
print('列表中大于3的元素有：',[item for item in filter(lambda x:x>3,[1,2,3,4,5])])
'''

# 偏函数
from functools import partial
def mod(n,m):
    return n % m
mod_by_100 = partial(mod,100)

print('自定义函数，100对7取余结果为：',mod(100,7))
print('偏函数，100对7取余结果为：',mod_by_100(7))



