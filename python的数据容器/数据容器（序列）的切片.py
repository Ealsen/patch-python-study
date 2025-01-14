my_list = [0, 1, 2, 3, 4, 5]
my_cut_list = my_list[1:4:1]   # 见下注释
# 对列表从元素1号位到4号位（不包括4号元素，如果将4空着就代表从1号到最后结束）的元素进行切片,步长为1
print(my_cut_list)

my_list1 = [0, 1, 2, 3, 4, 5]
my_list_cut1 = my_list1[:]  # 从0号开始到结束，步长不写默认为1
print(my_list_cut1)

print(my_list1[::2])  # 从头到尾切片，步长为2

print(my_list1[::-1]) # 从头到尾结束，步长为-1

print(my_list1[3:1:-1])

print(my_list1[::-2])

print((0, 1, 2, 3, 4, 5)[1:4:1])

print("12345"[1:4:1])