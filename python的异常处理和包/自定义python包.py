'''
什么是Python包
从物理上看，包就是一个文件夹，在该文件夹下包含了一个_init_.py文件，
该文件夹可用于包含多个模块文件从逻辑上看，包的本质依然是模块
快速入门
步骤如下:
新建包~my _package
新建包内模块:my _module1~和^my_module2
包的作用：
当我们的模块文件越来越多时,包可以希助我们管理这些模块，
包的作用就是包含多个模块，但包的本质依然是模块
详情看老师视频p96[2:56]
https://www.bilibili.com/video/BV1qW4y1a7fU/?p=96&spm_id_from=pageDriver&vd_source=338e2dd944c2ac6aa2f76cbb27959c74
'''


# import my_package1.plan1
# import my_package1.plan2

# my_package1.plan1.hello()
# my_package1.plan2.haha()


# from my_package1 import plan1
# from my_package1 import plan2

# plan1.hello()
# plan2.haha()


# from my_package1.plan1 import hello
# from my_package1.plan2 import haha
# hello()
# haha()


# # 导入包
# from my_package1 import *
# # 通过__all__变量，控制import *
# # 方式:
# # 注意:必须在`_init_.py`文件中添加`_all__ = []`，控制允许导入的模块列表from包名import*
# # 模块名.目标
# # my_module1报红证明不可用
# 注意:
# # all__针对的是' from ... import *‘这种方式


'''
总结
1.什么是Python的包?
包就是一个文件夹，里面可以存放许多Python的模块（代码文件)，通
过包，在逻辑上将一批模块归为一类，方便使用。
2._init__.py文件的作用?
创建包会默认自动创建的文件，通过这个文件来表示一个文件夹是Python的包，而非普通的文件夹。
3._all_变量的作用?
同模块中学习到的是一个作用，控制import*能够导入的内容
'''