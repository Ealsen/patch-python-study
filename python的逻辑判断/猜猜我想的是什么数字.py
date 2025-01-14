sum = 5
print("猜数字游戏，输入1~5之间的一个数字。")
if int(input("输入你猜想的数字：")) == sum:
    print("恭喜你猜对了！")
elif int(input("你猜错了，再试一次")) == sum:
    print("恭喜你猜对了！")
elif int(input("这是最后一次机会了")) == sum:
    print("恭喜你猜对了！")
else:
    print("soryy,我想的数字是5")
