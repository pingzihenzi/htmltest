import sys
from sys import argv,path
'''
1、python用import或from ... import来导入相应的模块
2、将整个模块导入，用import module_name
3、从某个模块导入某个函数，用from somemodule import somefunction
4、从某个模块导入多个函数，用from somemodule import func1,func2,func3...
5、将某个模块中的全部函数导入，用from somemodule import *
'''

#导入sys模块,见python文件头
# print('================ Python import mode ================')
# print('命令行参数为：')
# for i in argv:
#     print(i)
# for j in path:
#     print('Path is: ',j)
# print('\n Python路径为：',sys.path)

#命令行参数
'''
通常，对于大型项目程序而言，执行程序的一个必要的步骤是正确处理命令行参数，这些命令行参数是提供给包含某参数化信息的程序或脚本的参数。
介绍三种常见的获取和解析命令行参数的方法
1、sys.argv
2、getopt需要使用script目录下的script_1文件
3、argparse需要使用script目录下的script_2文件
'''

print("正在运行的脚本名称：'{}'".format(sys.argv[0]))
print("脚本的参数数量：'{}'".format(len(sys.argv)))
print("脚本的参数是：'{}'".format(str(sys.argv)))