"""
为什么要捕获异常
世界上没有完美的程序，任何程序在运行的过程中，都有可能出现:异常，也就是出现bug
导致程序无法完美运行下去。
我们要做的，不是力求程序完美运行。
而是在力所能及的范围内，对可能出现的bug，进行提前准备、提前处理。
这种行为我们称之为:异常处理（捕获异常)
为什么需要捕获异常
当我们的程序遇到了BUG，那么接下来有两种情况:
①整个程序因为一个BUG停止运行
②对BUG进行提醒，整个程序继续运行
显然在之前的学习中，我们所有的程序遇到BUG就会出现①的这种情况，也就是整个程序直接奔溃.
但是在真实工作中，我们肯定不能因为一个小的BUG就让整个程序全部奔溃，也就是我们希望的是达到
②的这种情况那这里我们就需要使用到捕获异常
捕获异常的作用在于:提前假设某处会出现异常，做好提前准备，当真的出现异常的时候，
可以有后续手段。
捕获常规异常的基本语法:
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
快速入门
需求:尝试以`r`模式打开文件，如果文件不存在，则以“w”方式打开。
try:
f = open('linux.txt' , 'r')
except:
f =open('linux.txt', 'w')
"""

try:
    f = open("E:/q12msdcsw.txt","r",encoding="UTF-8") 
    f.read()
    f.close()
except:
    print("程序运行异常，请将文件模式改为“w”")

""" 
捕获指定异常
基本语法:
try:
    print(name)
except NameError as e:
    print('name变量名称未定义错误')
    print(e)
注意事项
如果尝试执行的代码的异常类型和要捕获的异常类型不一致，
则无法捕获异常。一般try下方只放一行尝试执行的代码。
"""

""" 
捕获多个异常
当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后，并使用元组的方式进行书写。
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('zeroDivision错误...')
"""

""" 
捕获所有异常
try:
    1/0
except Exception as e :
    print("出现异常了")
"""

""" 
异常的else语法
try :
    print( "Hello")
except Exception as e:
    print("出现异常了")
else:
    print("好高兴，没有异常。")
"""

""" 
异常的finally
finally表示的是无论是否异常都要执行的代码，例如关闭文件。
try:
    f = open( 'test.txt , 'r')
except Exception as e:
    f = open('test.txt" , 'w")
else:
    print('没有异常，真开心')
finally:
    f.close()
"""

""" 
总结
1.为什么要捕获异常?
2.捕获异常的语法?
3.如何捕获所有异常?
"""