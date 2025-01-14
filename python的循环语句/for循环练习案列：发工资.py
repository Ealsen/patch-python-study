money = 10000
for i in range(1,21):

    import random
    score = random.randint(1,10)

    if score < 5:
        print(f"员工{i}，绩效分为{score}，低于5，不发工资，下一位。")
        continue

    if money >= 1000:
        money -= 1000
        print(f"员工{i}，绩效分为{score}，高于5，发放1000元工资，公司账户余额还剩{money}元。")
    else:
        print(f"公司账户余额{money}。余额不足，再来下个月再来一并补发。")
        break