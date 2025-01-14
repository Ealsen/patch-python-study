# p111
# 设计一个类
class Student:
    name = None
    age = None
    gender = None
    st_id = None

# 创建对象
st_u1 = Student()
st_u2 = Student()

# 输入数据
st_u1.name = '张三'
st_u1.age = '18'
st_u1.gender = '男'
st_u1.st_id = '20230817'

st_u2.name = '王五'
st_u2.age = '19'
st_u2.gender = '男'
st_u2.st_id = '20221084'

# 打印
print(st_u1.name + '\n' + st_u1.age + '\n' + st_u1.gender + '\n' + st_u1.st_id + '\n')