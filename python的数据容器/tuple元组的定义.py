# 用变量接收一个元组
from operator import index


tuple1 = ("yuansu", "yuansu", True, "ealsen", 23, 12.3)
print(tuple1)
print(type(tuple1))

print("----------------------")

# 定义只有一个元素的元组
tuple4 = ("python",)  # 元组只有一个元素时，必须要在最后一个元素后面加逗号，不然不是元组
print(type(tuple4))
# 定义空元组
tuple2 = ()
tuple3 = tuple()
print(tuple2)
print(tuple3)
# 元组 tuple 与 列表 list 的语法差不多但它是不能被修改的

print("-----------嵌套-----------------")

# 元组的嵌套
tuple5 = ((1, 2, 3, 4), (3, 4, 5))
print(tuple5)
# 取出并打印 元组5 中的数字5
print(tuple5[1][2])
print(type(tuple5[1][2]))

print("-----------index-------------------")

# 查找 元组1 中的某个元素
num1 = tuple1.index("ealsen")
print(num1)

print("--------count---------------------")

# 统计 元组1 中某个元素的个数
num2 = tuple1.count("yuansu")
print(num2)

print("--------len---------------------")

# 用函数 len 统计 元组1 中总共有多少元素
num3 = len(tuple1)
print(num3)

print("----------元组的遍历while-----------------")

# 元组的遍历
index = 0
while index < len(tuple1):
    yuansu = tuple1[index]
    print(yuansu)
    index += 1

print("-----------元组的遍历for----------------------")

for yuansu in tuple1:
    print(yuansu)

print("-----元组内嵌套的列表是可以被修改的------")

# 元组内嵌套的列表是可以被修改的
tuple6 = (2, 3, [4 , 5])
print(tuple6)
tuple6[2][0] = "ealsen"
print(tuple6)