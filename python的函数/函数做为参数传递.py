"""
函数作为参数传递
在前面的函数学习中，我们一直使用的函数，都是接受数据作为参数传入:·数字
·字符串
·字典、列表、元组等
其实，我们学习的函数本身，也可以作为参数传入另一个函数内。
如下代码:
def test_fund(compute) :
    result = compute(1,2)
    print(result)
def compute(x，y):
    return x + y
test_func(compute)
#结果:3
函数compute，作为参数，传入了test_func函数中使用。
. test_func需要一个函数作为参数传入，这个函数需要接收2个数字进行计算，计算逻辑由这个被传入函数决定compute函数接收2个数字对其进行计算，compute函数作为参数，传递给了test_func函数使用
·最终，在test func函数内部，由传入的compute函数，完成了对数字的计算操作.
所以，这是一种，计算逻辑的传递，而非数据的传递!
就像上述代码那样，不仅仅是相加，相见、相除、等任何逻辑都可以自行定义并作为函数传入。
"""

# 定义一个函数.接收另一个函数作为传入参数
def test_func(compute):
    result = compute(1,2)
    print(f'compute参数的类型是：{type(compute)}')
    print(f'计算结果：{result}')

# 定义一个函数，准备作为参数传入另一个函数
def compute(x,y):
    return x + y

# 调用,并传入两数
test_func(compute)

""" 
总结
1.函数本身是可以作为参数，传入另一个函数中进行使
用的。
2.将函数传入的作用在于:传入计算逻辑，而非传入数
据。
"""