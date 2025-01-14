"""
课后练习:单词计数
通过Windows的文本编辑器软件，将如下内容，复制并保存到: testword_1.txt，
文件可以存储在任意位置

itheima itcast python 
itheima python itcast 
beijing shanghai itheima
shenzhen guangzhou itheima
wuhan hangzhou itheima
zhengzhou bigdata itheima

通过文件读取操作，读取此文件，统计itheima单词出现的次数.
"""

f = open("python对于文件的应用/testword_1.txt","r",encoding="UTF-8")
wordsence = f.read()
a = wordsence.count("itheima")
f.close
print(f"在打开的文件testword_1.txt中，itheima出现了：{a}次")