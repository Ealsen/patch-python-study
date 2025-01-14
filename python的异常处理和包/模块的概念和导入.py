"""
python的模块
什么是模块
Python模块(Module)，是一个Python 文件，以.py结尾．模块能定义函数，
类和变量模块里也能包含可执行的代码
模块的作用: python中有很多各种不同的模块，每一个模块都可以帮助我们
快速的实现一些功能，比如实现和时间相关的功能就可以使用time模块我们
可以认为一个模块就是一个工具包，每一个工具包中都有各种不同的工具供
我们使用进而实现各种不同的功能.
大白话:模块就是一个Python文件，里面有类、函数、变量等，我们可以拿
过来用（导入模块去使用)
模块的导入方式
模块在使用前需要先导入导入的语法如下:
[from模块名] import[模块|类│变量|函数│*] [as别名]常用的组合形式如:
import模块名
from模块名 import 类、变量、方法等
from模块名 import *
import模块名 as 别名
from模块名import功能名as别名
import模块名
基本语法:
import模块名
import模块名1，模块名2模块名.功能名()
案例:导入time模块
#导入时间模块
import time
print("开始")
#让程序睡眠1秒(阻塞)
# time.sleep(1)
print("结束")
"""

import time    # 导入Python内置的time模块(time.py这个代码文件)

print("Loading...")  
time.sleep(3)       # 通过．就可以使用模块内部的全部功能（类、函数、变量)
print("Loading complete")

"""
from模块名import功能名
基本语法:
from模块名import 功能名功能名()
案例:导入time模块中的sleep方法
# 导入时间模块中的sleep方法
from time import sleep
print("开始")
# 让程序睡眠1秒(阻塞)
sleep(1)
print("结束")
"""

"""
# 使用*导入time模块的全部功能
# from time import *
# *表示全部的意思
"""

"""
基本语法:# 模块定义别名
# import模块名as别名
# 功能定义别名
# from模块名import功能as别名案例:
# 使用as给特定功能加上别名
# import time as t
# print(”你好")
# t.sleep(5)
# print("我好")
"""

"""
总结
1.什么是模块?
模块就是一个Python代码文件，内含类、函数、变量等，我们可以导入
进行使用。
2.如何导入模块
[from模块名]import[模块│类│变量│函数│*][as别名]
3.注意事项:
from可以省略，直接import即可
as别名可以省略
通过”.”来确定层级关系
模块的层入一般易在线码文件的开头位置
"""