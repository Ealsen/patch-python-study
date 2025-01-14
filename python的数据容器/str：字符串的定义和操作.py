my_str = "itheima and itcast"

value = my_str[2]
value2 = my_str[-16]

print(value)
print(value2)

print("------------------")

# index
print(my_str.index("and"))

# 同元组一样，字符串也是无法修改的,但是可以通过从老字符串的基础上得到一个新的字符串
# replace
new_my_str = my_str.replace("it","程序")  # 将“it”替换成“程序”
print(my_str)
print(new_my_str)

# spilt
my_str_list = my_str.split(" ") # 以一个空格来拆分字符串 my_str 形成列表
print(my_str_list)

# strip
my_str1 = " ealsen and ealsao "
print(my_str1)
strp_my_str = my_str1.strip() # 不传入参数就是去除首尾空格
print(strp_my_str)

print("--------------------")

my_str2 = "12ealsen and ealsao21"
print(my_str2)
strp_my_str1 = my_str2.strip("12") # 传入参数12就是取除首12尾21，也就是说这里把12看成两个字符
print(strp_my_str1)

# 统计e在 my_str1 出现了多少次
print(my_str1.count("e"))

# 统计 my_str1 的长度
print(len(my_str1))

# 字符串的遍历
index = 0
while index < len(my_str1):
    print(my_str1[index])
    index += 1

print("-----------------------------------")

for yuansu in my_str1:
    print(yuansu)