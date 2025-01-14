my_set = {"传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima"}
my_set_empty = set()     # 定义空集合
print("1:",my_set,"1:",type(my_set))
print("2:",my_set_empty,"2:",type(my_set)) # 集合无序且不重复，不支持下标索引，但支持修改

# add
my_set.add("python")
print("3:",my_set)

# remove
my_set.remove("黑马程序员")
print("4:",my_set)

# pop 由于不支持下标索引，pop代表随机取出一个元素
print("5:",my_set.pop())
print("6:",my_set)

my_set = {"传智教育", "黑马程序员", "itheima"}

# clear
print("7:",my_set)
print("7:",my_set.clear())

# 取2个集合的差集(集合1有的，而集合2没有的)
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print("8:",set3)

# 消除2个集合的交集（在集合1内，删除和集合2相同的元素，集合1被修改，集合3不变）
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print("9",set1,"|",set2)

# 2个集合的合并
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print("10:",set1,"|",set2,"|",set3)

# 统计集合元素的数量
set1 = {1, 2, 3, 4, 5, 6}
count1 = len(set1)
print("11:",count1)

# set 的遍历(由于set不支持下标索引，所以不能用while循环)
set1 = {1, 2, 3}
for x in set1:
    print("12:",x)