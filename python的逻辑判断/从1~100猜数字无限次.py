import random
num = random.randint(1,100)

count = 0
flag = True

while flag:
    guess_num = int(input("请输入你猜的数字（1~100）："))
    count += 1
    if guess_num == num:
        print("你猜对了！")
        flag = False
    else:
        if guess_num > num:
            print("你猜大了！")
        else:
            print("你猜小了！")

print(f"你猜了：{count}次")
