str1 = "python"
str2 = "ealsen"
str3 = "gtasa"

count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度为{count}。")

count = 0
for i in str2:
    count += 1
print(f"字符串{str2}的长度为{count}。")

count = 0
for i in str3:
    count += 1
print(f"字符串{str3}的长度为{count}。")

print("---------------------------------------------------------")

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度为{count}。")

my_len(str1)
my_len(str2)
my_len(str3)

