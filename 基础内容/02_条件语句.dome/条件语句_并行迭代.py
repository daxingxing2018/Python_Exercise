student=['xiaomeng','xiaozhi','xiaoqiang']
number=[1001,1002,1003]

for i in range(len(student)):
    print(student[i],'的学号是：',number[i])

for name,num in zip(student,number):
    print(name,'的学号是：',num)

for num1,num2 in zip (range(3),range(100)):
    print('zip的键值对为：',num1,num2)