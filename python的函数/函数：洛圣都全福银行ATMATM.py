money = 50000
name = None

name = input("请输入您的用户名：")

def chaxun(head):
    if head == True:
        print("------查询余额------")
    print(f"{name}，您好，您的余额剩余：{money}元。")

def qukuan(num):
    global money
    money -= num
    print(f"{name}，您好，您取款{num}元成功。")
    chaxun(False)

def cunkuan(num):
    global money
    money += num
    print(f"{name}，您好，您存款{num}元成功。")
    chaxun(False)

def zhucaidan():
    print("----------主菜单----------")
    print(f"{name}欢迎来到洛圣都全福银行ATM，请选择你的操作：")
    print("查询余额【输入1】")
    print("存款\t【输入2】")
    print("取款\t【输入3】")
    print("退出\t【输入4】")
    return input("请输入你的选择:")

while True:
    Keyboard_input = zhucaidan()
    if Keyboard_input == "1":
        chaxun(True)
        continue
    elif Keyboard_input == "2":
        num = int(input("您想要存多少钱？请输入："))
        cunkuan(num)
        continue
    elif Keyboard_input == "3":
        num = int(input("您想要取多少钱？请输入："))
        qukuan(num)
        continue
    else:
        print("程序退出啦")
        break