def say_hi():
    print("hi,i am ealsen.")
    # def不写返回依然有返回值None（自动补充返回None）

result = say_hi()

print(result)

print(type(result))

print("----------------")

def say_hi():
    print("hi,i am ealsen.")
    # 这里写了返回None
    return None

result = say_hi()
print(result)
print(type(result))

print("------------------------")

# None在if判断中，None等同于False
if result:
    print("1yes!")

True_result = True

if True_result:
    print("2yes!")

False_result = False

if False_result:
    # 我们都知道，在if中，如果为False，那么下面的代码将不会执行
    print("1yes!")
    
print("-------------------------------------")    
# 当一个变量暂时不需要其有具体值时，可以用None代替
dingyi_Num = None
print(dingyi_Num)