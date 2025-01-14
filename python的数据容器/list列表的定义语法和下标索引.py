my_list = ["str", True, 123, 11.3205]
print(my_list)
print(type(my_list))

my_list_add = ["python", 9090.678, my_list, 23]  # 列表可以嵌套
print(my_list_add)
print(type(my_list_add))

print(my_list[1])
print(my_list[0])
print(my_list[-1])
print(my_list[-2])
# 不要超过下标索引的范围，否则会报错
# print(my_list[-5])
print(my_list_add[2])  # 相当于打印 my_list
print(my_list_add[2][0])  # 相当于打印 my_list 里面的0号元素

print(type(my_list[1]))