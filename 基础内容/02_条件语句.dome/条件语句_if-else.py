greeting='hello'
if greeting == 'hello':
    student={'小萌':'1001','小红':'1002','小强':'1003'}
    print('字典元素的个数为：%d个'%len(student))
    student.clear()
    print('字典删除后的元素个数为：%d个'%len(student))

if greeting == 'hi':
    print('hi')
else:
    print('该语句块不在if中，greeting的值不是hi')

num = 10
if num>10:
    print('num的值大于10')
elif 0<=num<=10:
    print('num的值介于0到10之间')
else:
    print('num的值小于0')

num = 8
if num%2==0:
    if num%3==0:
        print('你输入的数字可以整除2和3')
    elif num%4==0:
        print('你输入的数字可以整除2和4')
    else:
        print('你输入的数字可以整除2，但不能整除3和4')
else:
    if num%3==0:
        print('你输入的数字可以整除3，但不能整除2')
    else:
        print('你输入的数字不能整除2和3')
