'''
. file_util.py(文件处理相关工具，内含:)
·函数:print_file_info(file_name)，接收传入文件的路径，打印文件的全部内
容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
·函数: append_to_file(file_name， data)，接收文件路径以及传入数据，将数据
追加写入到文件中
'''


def print_file_info(file_name):
    '''
    功能是:将给定路径的文件内容输出到控制台中
    : param file_name:即将读取的文件路径
    : return: None
    '''
    f = None
    try:

        f = open("file_name", "r", encoding="utf-8")

        content = f.read()
        print(f"文件的全部内容：{content}")
    except Exception as e:
        print(f"错误为：{e}")
    finally:
        if f:         # 如果变量是None，表示False，如果有任何内容，就是True
            f.close() # 关闭

def append_to_file(file_name,data):
    '''
    功能:将指定的数据追加到指定的文件中
    : param file_name:指定的文件的路径
    : param data:指定的数据
    : return: None
    '''
    f = open("file_name", "a", encoding="utf-8")
    f.write(data)
    f.close()


# 测试
if __name__ == '__main__':
    print_file_info("E:\\zzz_Ealsen_wenjian\\daimazzzcode\\zzzcodepython\\黑马程序员Python8天从入门到精通\\ReadMe.md")   # E:\zzz_Ealsen_wenjian\daimazzzcode\zzzcodepython\黑马程序员Python8天从入门到精通\ReadMe.md
    # append_to_file("", "")