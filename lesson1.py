import keyword
import sys
'''
1、第一個字符必須是字母或下劃綫
2、標識符的其他部分由字母、數字和下劃綫組成
3、標識符對大小寫敏感
'''
# print(keyword.kwlist)
#python中的單行注釋以#開頭
#多行注釋可以用多個#分行，也可以用''' '''或""" """ 

#行與縮進
# 同一個代碼塊的語句必須包含相同的縮進空格數

#多行語句，如果語句很長，可以使用反斜杠‘\’來實現多行語句
# total = 123 +\
#     234 +\
#         345
# print(total)

#python中的單引號和雙引號使用完全相同
#可以使用三引號'''或"""可以指定一個多行字符串
#使用\進行轉義
#也可以使用r來使轉義失效，例如r"this is a line with \n",r就是raw string哎
#字符串不能改變，字符串截取的語法格式 var[頭下標:尾下標:步長]
str = '''123456789'''
print(str[2:5]) #這個的意思是，從下標索引2開始，包括2，到索引6，但不包括6對應的數字。所以輸出是345
# print('hello\nworld')
# print(r'hello\nworld')

#空行主要用于区分代码块，python并不会对空行进行处理

#用户输入
# input("enter your word:\n")

sys.stdout.write("hi")
sys.stdout.write(str)