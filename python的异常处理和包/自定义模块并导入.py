"""
制作自定义模块
Python中已经帮我们实现了很多的模块．不过有时候
我们需要一些个性化的模块，这里就可以通过自定义模块实现，
也就是自己制作一个模块
注意:
每个Python文件都可以作为一个模块，模块的名字就是文件的名字．
也就是说自定义模块名必须要符合标识符命名规则
"""
# 简单的导入自己的测试模块并使用
import my_test_module1
my_test_module1.test()
# 或者用from my_module1导入test
# from my_module1 import test
# test()
# 如果导入两个同名的功能，后面导入的会覆盖掉前面导入的
print("成功导入并使用自定义模块my_test_module1")

"""
测试模块
在实际开发中，当一个开发人员编写完一个模块后，为了让模块能够
在项目中达到想要的效果，这个开发人员会自行在py文件中添加一些
测试信息，例如，在my_modulel.py文件中添加测试代码test(1, 1)
def test(a, b):
    print(a + b)
test(1,1)
问题:
此时，无论是当前文件，还是其他已经导入了该模块的文件，
在运行的时候都会自动执行'test`函数的调用
解决方法：
运行一下自定义模块my_test_module4.py
你大概就明白了
"""

'''
_all
如果一个模块文件中有`_all_`变量，
当使用`from xxx import(导入时，只能导入这个列表中的元素
详情看my_test_module5.py
'''

# __all__ = ['testa']     
# # 如果一个模块文件中有`_all_`变量，当使用`from xxx import(*)导入时，
# # 只能导入这个列表中的元素

# def testa():
#     print("testa")

# def testa():
#     print("testb")


''' 
总结
1.如何自定义模块并导入?
在Python代码文件中正常写代码即可，通过import、 from关键字和
导入Python内置模块一样导入即可使用。
2._main_变量的功能是?
if _main_== "_main_”表示，只有当程序是直接执行的才会进入if内部，
如果是被导入的，则if无法进入
3.注意事项
·不同模块，同名的功能，如果都被导入，那么后导入的会覆盖先导
入的
 _all_变量可以控制import*的时候哪些功能可以被导入
'''