def add(x,y):
    result = x + y
    print(f"{x}+{y}的结果是{result}")

add(5,3)
add(5,9)
add(2,3)

print("--------------")
# 以下是定义一个函数规范的写法
def add(x,y):
    """
    add可以接收两个参数进行相加
    :param x: 形参x表示相加的其中一个数字
    :param y: 形参y表示相加的另一个数字
    :return: 返回值是两数相加的结果
    """
    result = x + y
    return result
    # 定义函数时，在return后面的代码都不会被执行
    print("我不会被执行，因为在return的后面")

i = add(12,67)
print(i)

