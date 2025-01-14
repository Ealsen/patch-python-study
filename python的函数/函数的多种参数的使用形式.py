# 函数的多种参数的使用形式

def usder_info(name, age, gender):
    print(f"您的名字是：{name},年龄是：{age},性别是：{gender}。")

# 关键字传参

usder_info(name="小明" , age=20 , gender="男")
# 可以不按照固定顺序
usder_info(age=20, gender="男", name="小明")
# 可以和位置参数混用，位置参数必须在前，且匹配参数顺序
usder_info("小明", age=20 , gender="男")

# 缺省参数(默认值必须是参数的最后面)

def usder_info(name, age, gender='男'):
    print(f"您的名字是：{name},年龄是：{age},性别是：{gender}。")

usder_info("小天",18)

# 不定长参数

# 位置传递
# 传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple),
# args是元组类型，这就是位置传递
def user_info_args(*args):
    print(args)

# ('Tom')
user_info_args('Tom')
# ('Tom', 18)
user_info_args("Tom", 18)

# 关键字传递
# 参数是“键=值”形式的形式的情况下，所有的“键=值”都会被kwargs接受,
# 同时会根据“键=值”组成字典!

def user_info_kwargs(**kwargs):
    print(kwargs)

# {'name':'Tom',' age ' : 18, 'id ' : 110}
user_info_kwargs(name='TOM', age=18, id=110)


"""
总结 
1.掌握位置参数
·根据参数位置来传递参数
2.掌握关键字参数
·通过“键=值”形式传递参数，可以不限参数顺序﹒可以和位置参数混用，位置参数需在前
3.掌握缺省参数
不传递参数值时会使用默认的参数值-默认值的参数必须定义在最后
4.掌握不定长参数
﹒位置不定长传递以*号标记一个形式参数，以元组的形式接受参数，形式参数一般命名为args
·关键字不定长传递以**号标记一个形式参数，以字典的形式接受参数，形式参数一般命名为kwargs
 """