count = [0 for _ in range(100)]

from timeit import Timer
####计数排序中的注意事项
# （1）数组列表中的数必须 >=0, <=100, 且为整数
# （2）在计数排序的过程中，最大值是先给定的，而不是在计数排序中找到的
# （3）计数排序的流程：
# a. 原始数组列表: len = n
# b. 计数数组列表：即字典，从0-最大值中，每个数出现了几次：len = 字典的len（max_value+1）
# c.累计数组列表：找到0-最大值中，每个数的index position是第几位: len = 字典的len(max_value+1)
# d.最终数组列表：len = 原始数组列表a的len = n


def countingsort(li,max_value):
    len_original = len(li)  #长度为n
    len_dict = max_value+1  #长度为k
    list_dict = [0 for _ in range(len_dict)] ###长度为len（max_value+1的0的列表【0, 0, 0, 0, 0....0】
    #构建列表字典，更新列表中的0
    for value in li:
        list_dict[value] += 1
    li.clear()
    for position, number in enumerate(list_dict):
        li += [position]*number   #（这里也可以改成append多少次）
        ####append多少次的写法：
        # for i in range(number):
        #     li.append(position)
    print(li)

def commonsort(li):
    li.sort()

li = [0,1,3,5,1,2,4,2]
max_value = 5
sort1 = countingsort(li,max_value)
sort2 = commonsort(li)
print(sort1)
print(sort2)
##时间复杂度为 O(n+k),即O(n)



####对比一下时间，用装饰器，两种方法
#（1）用timer

# t1 = Timer('countingsort([for i in range(10000)]], 5)','from __main__ import countingsort')
#
# #time_common = Timer('li.sort()')
# t2= Timer('commonsort([0,1,3,5,1,2,4,2])','from __main__ import commonsort')
#
# print(t1.timeit(1000))
# print(t2.timeit(1000))


#方法2 装饰器
####具体下次再说
index = 1
list_one_to_ten = [[] for _ in range(10)]
li = [910,281,89011,2382,87,8,1]
li2 = []
for value in li:
    str_value = str(value)
    str_value = "0" * (5 - len(str(value))) + str(value)
    #print(str_value)
    li2.append(str_value)
li = li2
#print(li)
#li2.clear()

####这个是基数分裂 redix sort
while index <= 5:

    for str_value in li:
        list_one_to_ten[int(str_value[-index])].append(str_value)
    #li.clear()
    #print(list_one_to_ten)
    li.clear()
    for small_list in list_one_to_ten:
        li += small_list
    for small_list in list_one_to_ten:
        small_list.clear()
    index += 1
print(li)
li3 = []
for value in li:
    li3.append(int(value))
print(li3)





