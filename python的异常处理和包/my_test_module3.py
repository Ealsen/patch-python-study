from my_test_module4 import test4
# 因为导入的模块已经再其模块内启用了test4的功能
# 所以导入的时候也会运行test4
# 解决方法可以参照my_test_module2
# 这里导入my_test_module2的test2试一试
from my_test_module2 import test2
# 这里可以看到并没有像test4一样运行

# def test2():
#     print("my_test_module2:test word2")
#     print("end")

# if __name__ == '__main__':   # 因为这句
#     test2()