__all__ = ['testa']     
# 如果一个模块文件中有`_all_`变量，当使用`from xxx import(*)导入时，
# 只能导入这个列表中的元素

def testa():
    print("testa")

def testa():
    print("testb")