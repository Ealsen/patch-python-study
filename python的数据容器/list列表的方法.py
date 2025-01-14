from itertools import count


my_list = ["ittest", "itheima", "python"]
index = my_list.index("itheima")
print(f"在my_list中itheima下标索引值是{index}")
# 如果查询的元素不存在就会报错

print("1----------------------------------------------------")

my_list[0] = "传智教育"  # 修改 my_list 的0号元素的内容
print(my_list)
my_list.insert(1,"best")  # 插入元素 best。注意：这里的下标1是插入后的下标
print(my_list)

my_list.append("ealsen")  # 在 list 最后面追加元素
print(my_list)

my_list.extend([213, 2345, 2343453454])  # 在 my_list 后面追加一个新的list
print(my_list)

print("2------------------------------------------------------")

# 元素的删除
del my_list[-1]
print(my_list)

my_list.pop(-1)  # pop 的本质是取出一个元素，它可以被变量接收
print(my_list)
pop = my_list.pop(0)
print(my_list)
print(pop)

print("3------------------------------------------------")

my_list.insert(-1,"best")
print(my_list)

# 删除某元素在列表中的第一个匹配项
my_list.remove("best")    # 删除了best
print(my_list)

print("4--------------------------------------------------")

# 清空列表
my_list.clear()
print(my_list)

print("5-------------------------------------------")

# 统计列表某元素的数量
list1 = [12, 23 , 45, 12, 12, 13, 13, 34]
count1 = list1.count(12)
print(count1)

# 通过函数 len 统计列表内元素的数量
count2 = len(list1)
print(count2)