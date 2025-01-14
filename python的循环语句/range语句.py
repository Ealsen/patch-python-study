# range（num）
# 获得一个从零开始到num结束但不包括num的数字序列
# 如 range(5) 得到的序列为[0,1,2,3,4]
for x in range(5):
    print(x)

print("----------------------------------")

# range(num1,num2)
# 获得一个从num1开始到num2结束但不包括num2的数字序列
# 如 rang(3,6) 得到的序列为[3,4,5]
for y in range(3,6):
    print(y)

print("----------------------------------")

# range(num1,num2,step)
# 获得一个从num1开始到num2结束但不包括num2的数字序列
# 其中step为步长,默认step为1
# 如 range(5,10,2)得到的序列为[5,7,9]c
for z in range(5,10,2):
    print(z)
