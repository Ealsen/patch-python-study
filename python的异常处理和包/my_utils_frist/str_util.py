'''
创建一个自定义包，名称为:my_utils(我的工具)在包内提供2个模块
. str_util.py(字符串相关工具，内含:)
·函数:str_reverse(s)，接受传入字符串，将字符串反转返回
·函数: substr(s,x, y)，按照下标x和y，对字符串进行切片
'''

def str_reverse(s):
    '''
    功能是将字符串完成反转
    : param s:将被反转的字符串
    : return:反转后的字符串
    '''
    ss = s[::-1]
    fstr = print(f"反转后的字符串：{ss}")
    return fstr


def substr(s,x,y):
    '''
    功能是按照给定的下标完成给定字符串的切片
    : param x:切片的开始下标
    : param y:切片的结束下标
    : return:切片完成后的字符串
    '''
    cutstr = s[x:y]
    cutstrcc = print(f"你输入的字符串为：{s}，切片后的字符串为：{cutstr}")
    return cutstrcc

# 测试
if __name__ == '__main__':
    print(str_reverse("小趴菜"))
    print(substr("小丑既然是我自己", 1, 3))