from curses import keyname
from multiprocessing.sharedctypes import Value
from unittest import result


my_dict1 = {"wlh":12, "sli":13, "ljj":15}
wlhscore = my_dict1["wlh"]
print(f"my_dict的内容是：",my_dict1,"，类型是：", type(my_dict1),"。")
print(f"wlh的分数为：",wlhscore,"。")

namescore_dict1 = {"wlh":{"yw":88,"sx":90,"yy":70},"zjl":{"yw":78,"sx":60,"yy":80},"ljj":{"yw":89,"sx":80,"yy":60}}

print(f"dict的嵌套，key里面不能包括字典类型。\n","namescore_dict1 = ",namescore_dict1)
print(f"zjl的语文成绩为：",namescore_dict1["zjl"]["yw"])
    
print(f"打印ljj的英语成绩：",namescore_dict1["ljj"]["yy"])