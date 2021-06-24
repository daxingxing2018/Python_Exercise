'''
游戏内容：
    随便给定一个在一定范围内的数字，让用户去猜这个数字是多少，并输入自己猜测的数字，系统判定给定的数字。
    输入的猜测数字大于给定值，提示输入的数字过大
    输入的猜测数字小于给定值，提示输入的数字过小
    输入的测试数字等于给定值，提示你猜对了，并展示猜了多少次猜中的
'''

import random

number = random.randint(1,100)
guess = 0
while True:
    num_input=input('请输入一个1到100的数字：')
    guess += 1
    if not num_input.isdigit():
        print("请输入数字。")
    elif int(num_input)<0 or int(num_input)>=100:
        print("输入的数字必须介于1到100。")
    else:
        if number == int(num_input):
            print("恭喜您，您猜对了，您总共猜了 %d 次"%guess)
            break
        elif number > int(num_input):
            print("您输入的数字过小了。")
        elif number < int(num_input):
            print('您输入的数字过大了。')
        else:
            print("系统发生不可预测的问题，请联系管理人员进行处理。")
