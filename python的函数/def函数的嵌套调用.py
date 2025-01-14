# 定义函数func_b
def func_b():
    print("---b---")

# 定义函数func_a
def func_a():
    print("---a---")
    # 嵌套函数func_b
    func_b()
    print("---c---")

# 调用函数func_a
func_a()