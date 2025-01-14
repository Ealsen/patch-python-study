# 随机生成1~10之间的一个整数
import random
num = random.randint(1,10)

# 打印游戏规则
print("""
      这是个猜数字的游戏。
      请在1~10中任意猜一个数字。
     """)

# 定义猜的数字的变量
guess_num = int(input("请输入你猜的数字"))

# 逻辑判断if的嵌套
if guess_num == num:
    print("恭喜你第一次就猜对了！")
    
else:
    if guess_num > num:
        print("你猜的大了！再试一下！")
    else:
        print("你猜的小了！再试一下！")
    
    guess_num = int(input("请输入你猜的数字"))

    if guess_num == num:
              print("恭喜你第二次就猜对了！")

    else:
        if guess_num > num:
            print("你猜的大了！再试一下！")
        else:
            print("你猜的小了！再试一下！")

        guess_num = int(input("请输入你猜的数字"))

        if guess_num == num:
            print("恭喜你第三次就猜对了！")

        else:
            if guess_num > num:
                print("你猜的大了！没有机会了！")
            else:
                print("你猜的小了！没有机会了！")

"""
实际上，以上逻辑判断部分可以用循环进行优化
"""

        


