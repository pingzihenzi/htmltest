import sys
import getopt

'''
getopt模块是专门用来处理命令行参数的模块，用于获取命令行选项和参数。命令行选项使得程序的参数更加灵活
支持短选项模式和长选项模式
hi:o:的解释为，h后面不带参数，i和o后面需要带参数
'''
def main(argv):
    input_file = ""
    output_file = ""
    temp_var = ""
    try:
        opts,args = getopt.getopt(argv[1:],"hci:o:",["help","input_file=","output_file="])
        for opt,arg in opts:
            if opt in ("-h","--help"):
                print('script_2.py -i <input_file> -o <output_file>')
                print('or:script_2.py --input_file=<imput_file> --output_file=<output_file>')
                sys.exit()
            elif opt in ("-i","--input_file"):
                input_file = arg
            elif opt in ("-o","--output_file"):
                output_file = arg
            elif opt in ("-c"):
                temp_var = arg
        print('输入文件为：',input_file)
        print('输出文件为：',output_file)
        print('输出的临时变量为：',temp_var)
        print(args)
        for i in range(0,len(args)):
            print('不含"-"或"--"的参数 %s 为：%s' %(i + 1,args[i]))
        # print(args[i])
    except getopt.GetoptError as e:
        print(e.msg)
        print(e.opt)
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv)