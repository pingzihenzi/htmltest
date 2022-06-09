import argparse

'''
当程序中使用复杂的参数，或多个文件名字的时候，建议使用python的argparse库
它以系统的方式处理命令行参数，更易于编写友好的程序
argparse库同样可以用于解析命令行参数，首先，由代码确定所需的参数，然后argparse将这些参数解析为sys.argv.
'''

parser = argparse.ArgumentParser()
parser.add_argument("h",help="this is a test")
args = parser.parse_args()