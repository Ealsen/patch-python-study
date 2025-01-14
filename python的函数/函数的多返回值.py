def test_return():
    print("函数的多返回值")
    return 1, "nihao", True

x, y, z = test_return()
print(x,y,z)