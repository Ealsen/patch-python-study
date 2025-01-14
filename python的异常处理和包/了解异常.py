"""
什么是异常
当检测到一个错误时，Python解释器就无法继续执行了，
反而出现了一些错误的提示，这就是所谓的“异常”，
也就是我们常说的BUG

bug单词的诞生
早期计算机采用大量继电器工作，马克二型计算机就是这样的。
1945年9月9日，下午三点，马克二型计算机无法正常工作了，技术人员试了很多办法，
最后定位到第70号继电器出错。负责人哈珀观察这个出错的继电器，发现一只飞蛾躺在中间，
已经被继电器打死。她小心地用摄子将蛾子夹出来，用透明胶布帖到“事件记录本”中，
并注明“第一个发现虫子的实例。”自此之后，引发软件失效的缺陷，便被称为Bug。
"""

f = open("E:/q12msdcsw.txt","r",encoding="UTF-8") 
# 以上是用r模式打开一个不存在的模式
f.read()
f.close()

""" 
运行之后的内容如下：
黑马程序员Python8天从入门到精通/python的异常处理和包/了解异常.py
Traceback (most recent call last):
  File "e:\zzz_Ealsen_wenjian\daimazzzcode\zzzcodepython\黑马程序员Python8天从入门到精通\python的异常处理和包\了解异常.py", line 15, in <module>
    f = open("E:/q12msdcsw.txt","r",encoding="UTF-8")
FileNotFoundError: [Errno 2] No such file or directory: 'E:/q12msdcsw.txt'
PS E:\zzz_Ealsen_wenjian\daimazzzcode\zzzcodepython\黑马程序员Python8天从入门到精通>
"""

""" 
总结
1.什么是异常:
异常就是程序运行的过程中出现了错误
2.bug是什么意思:
bug就是指异常的意思，因为历史因为小虫子导致计算机失灵的案例，所以延续至今，bug就代表软件出现错
误。
"""