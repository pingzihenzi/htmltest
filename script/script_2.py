import argparse
from tabnanny import check

'''
当程序中使用复杂的参数，或多个文件名字的时候，建议使用python的argparse库
它以系统的方式处理命令行参数，更易于编写友好的程序
argparse库同样可以用于解析命令行参数，首先，由代码确定所需的参数，然后argparse将这些参数解析为sys.argv.
argsparse会将传递的参数默认为字符串，可以通过加上参数type=int来将传递参数视为整数
'''

parser = argparse.ArgumentParser()
parser.add_argument("-echo",help ="echo the argument you input")
parser.add_argument("-square",type=int,help="display a square of a given number")
parser.add_argument("-v","--verbose",action="store_true",help="increase output verbosity")
args = parser.parse_args()

if args.verbose:
    print("verbosity turned on")
print("Argument you inputed is:",args.echo)
print("Square number is:",args.square**2)


