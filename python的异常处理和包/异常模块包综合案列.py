'''
p98
练习案例:自定义工具包
创建一个自定义包，名称为:my_utils(我的工具)在包内提供2个模块
. str_util.py(字符串相关工具，内含:)
·函数:str_reverse(s)，接受传入字符串，将字符串反转返回
·函数: substr(s,x, y)，按照下标x和y，对字符串进行切片
. file_util.py(文件处理相关工具，内含:)
·函数:print_file_info(file_name)，接收传入文件的路径，打印文件的全部内
容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
·函数: append_to_file(file_name， data)，接收文件路径以及传入数据，将数据
追加写入到文件中

构建出包后，尝试着用一用自己编写的工具包。
'''

from my_utils_frist.file_util import *
from my_utils_frist.str_util import *

# str_reverse("你好呵")
# substr("abcdefghijkllnopqrst",5,12)