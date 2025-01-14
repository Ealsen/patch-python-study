""" 
文件的追加操作:
#1.打开文件，通过a模式打开即可f = open('python.txt' , "a')
#2.文件写入
f.write('hello world')
#3.内容刷新
f.flugh()
注意:
a模式,文件不存在会创建文件
a模式,文件存在会在最后，追加写入文件
"""

f = open("./python对于文件的应用/test_word3.txt","a",encoding="UTF-8")
# 如以上文件不存在，会创建新文件
f.write("hello word!!!")    # 将内容写入内存中
# f.flush()     # 将内存中积累的内容写入硬盘文件中
f.close()     # close里面内置了flush的功能

f = open("./python对于文件的应用/test_word3.txt","a",encoding="UTF-8")
# 如以上文件不存在，会创建新文件
f.write("I am Python.")    # 将内容写入内存中
# f.flush()     # 将内存中积累的内容写入硬盘文件中
f.close()     # close里面内置了flush的功能

f = open("./python对于文件的应用/test_word3.txt","a",encoding="UTF-8")
# 如以上文件不存在，会创建新文件
f.write("\nHappy!")    # 换行，再将内容写入内存中
# f.flush()     # 将内存中积累的内容写入硬盘文件中
f.close()     # close里面内置了flush的功能

""" 
1.追加写入文件使用open函数的”a”模式进行写入
2.追加写入的方法有（和w模式一致）∶
. wirte()，写入内容
. flush()，刷新内容到硬盘中
3.注意事项:
·a模式，文件不存在，会创建新文件
·a模式，文件存在，会在原有内容后面继续写入· 可以使用”\n”来写出换行符
"""