num = 0
while num <3:
    print(num,'小于3')
    num = num + 1
else:
    print(num,"大于或等于3")
print("结束循环！")

names = ['xiaomeng','xiaozhi']
for name in names:
    if name == 'xiao':
        print('名称：',name)
        break
    print("循环名称列表" + name)
else:
    print('没有循环的数据！')
print("结束循环！")