i = 1 
for i in range(1,10):
    
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t",end='')
        j += 1
    i += 1
    print() # 空内容，print()可以看作是换行
