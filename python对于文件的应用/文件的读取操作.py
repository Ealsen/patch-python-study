"""
什么是文件？
内存中存放的数据在计算机关机后就会消失。
要长久保存数据，就要使用硬盘、光盘、U盘等设备。
为了便于数据的管理和检索，引入了“文件”的概念。
一篇文章、一段视频、一个可执行程序，都可以被保存为一个文件，
并赋予一个文件名。操作系统以文件为单位管理磁盘中的数据。一般来说，
文件可分为文本文件、视频文件、音频文件、图像文件、可执行文件等多种类别。
想想我们平常对文件的基本操作，
大概可以分为三个步骤（简称文件操作三步走):1打开文件
2读写文件3关闭文件
在Python，使用open函数，可以打开一个已经存在的文件，或者创建一个新文件，
语法如下open(name, mode, encoding)
name:是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。
mode:设置打开文件的模式(访问模式):只读、写入、追加等。
encoding:编码格式（推荐使用UTF-8)
示例代码:
f = open('python.txt" , 'r', encoding=”UTF-8)
# encoding的顺序不是第三位，所以不能用位置参数，用关键字参数直接指定
注意事项
注意:此时的`f 是`open'函数的文件对象，对象是Python中一种特殊的数据类型，
拥有属性和方法，可以使用对象.属性或对象.方法对其进行访问，
后续面向对象课程会给大家进行详细的介绍。
mode常用的三种基础访问模式
r:以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
w:打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，
原有内容会被删除。w里该文件不存在，创建新文件。
a:打开一个文件用于追加。如果该文件已存在，新的内容将会被写入到已有内容之后。
如果该文件不存在，创建新文件进行写入。
"""
f = open("../黑马程序员Python教程/ReadMe.txt","r",encoding="UTF-8")
print(type(f))
print(f"读取文件并打印，内容为：{f.read(32)}") # read()里面传入参数代表读取多少字节
f.close

f = open("../黑马程序员Python教程/ReadMe.txt","r",encoding="UTF-8")
print(type(f))
print(f"读取文件并打印，内容为：{f.readline(2)}") 
# readline()里面传入参数代表读取多少行
# readlines()里面不传入参数，读取全部内容
# 还可以通过for循环来读取行数，{for line in f：}
f.close

with open("../黑马程序员Python教程/ReadMe.txt","r",encoding="UTF-8") as f:
    print(type(f))
    for line in f:
        print(f"读取文件内容的每一行并打印，内容为：{line}") 
# with open执行完毕自动close

"""
文件对象=open(file, mode, encoding)
打开文件获得文件对象
文件对象read(num)
读取指定长度字节不指定num读取文件全部
文件对象.
readline()
读取一行
文件对象.readlines()
读取全部行，得到列表
for line in文件对象
for循环文件行，一次循环得到一行数据
文件对象.close()
关闭文件对象
with open() as f
通过with open语法打开文件，可以自动关闭
总结
1.操作文件需要通过open函数打开文件得到文件对象
2.文件对象有如下读取方法:
 read()
readline()readlines()
.for line in文件对象
3.文件读取完成后，要使用文件对象.close()方法关闭文件对象，否则文件会被一直占用
"""