list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
list2 = []
index = 0
while index < len(list1):
    yuansu = list1[index]
    if yuansu % 2 == 0:
        list2.append(yuansu)
    index += 1

print(list2)

print("---------------------------------------")

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
list4 = []
for yuansu in list3:
    if yuansu % 2 == 0:
        list4.append(yuansu)

print(list4)
