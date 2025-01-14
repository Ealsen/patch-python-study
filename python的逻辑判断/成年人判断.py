print("欢迎来到黑马儿游乐场，儿童免票，成人收费。")
age = input("请输入你的年龄")
age = int(age)
print(f"您的年龄是：{age}岁")
if age >= 18:
    print("您已经成年，游玩需要补票10元。")
else:
    print("您是未成年，游玩免费。")
print("祝您游玩愉快！")