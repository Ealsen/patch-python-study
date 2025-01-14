num = 100000000000000

def testA():
    print(num)

print("-----------------")

def testB():
    # 设置testB里面的num为全局变量
    global num
    num = 100
    print(num)

print("--------------------")

def testC():
    str1 = "ealsen study python."
    print(f"第一次打印{str1}")

testA()
testB()
testC()
print("------------------------------------")
# 由于这里的str1是函数testC里面的局部变量，所以找不到str1，打印不了
# print(str1)