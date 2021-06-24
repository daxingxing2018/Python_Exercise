for letter in 'hello':
    if letter == 'l':
        break
    print('当前字母为：',letter)

for letter in 'hello':
    if letter == 'l':
        continue
    print("当前字母是：",letter)

num = 10
while num > 0:
    print('输出的数字为：',num)
    num -= 1
    if num == 8:
        break
num = 3
while num > 0:
    num -= 1
    if num == 2:
        continue
    print("当前的数字是: ",num)