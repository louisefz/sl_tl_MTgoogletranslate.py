# coding=utf-8
print("你好世界")


if True:
    print(1)
else:
    print(2)



# 单行注释的使用
print(1) # 测试使用

#用'''或者"""标示多行注释
print(1)
'''
这是多行注释，使用单引号
这是多行注释，使用单引号
'''

"""
这是多行注释，使用双引号
这是多行注释，使用双引号
"""


# 换行，同一行转化成多行

string = '1\n2\n3\n4\n5'
print(string)


# print实现不换行（换行是默认的）
x = 1
y = 2
print (x,)
print (y,)

print("hello", "world")
('hello', 'world')


# 多变量赋值
# （1）多变量赋值相同
A = B = C = 1
# (2)多变量分别赋值不同的值
A, B, C = 1, 2, 3

a, b = 0, 1
while b < 2000:
    print(b, end=",")
    a, b = b, a+b



print(2/3)
print(167//3)




naam = input ('What is your name?')
print('Hello, ' + naam + '!')


list['a', 'b', 'c', 'f']
print(list[])
