# 确认数字有几位数的方法：
# （1）
print(len(str(10000)))
# （2）
# 用lg函数向下取取整
# 1、向下取整： int()
# 2、向上取整：ceil()
# 3、四舍五入：round()
import math
print(int(math.log(1000, 10)))


#（3）方法3
iteration = 0
while 10 ** iteration < 100:
    iteration += 1
print(iteration)


print([[] for _ in range(10)])



def redixsort(li):
    index = 1
    list_one_to_ten = [[] for _ in range(10)]
    li = [910, 281, 89011, 2382, 87, 8, 1]
    li2 = []
    for value in li:
        str_value = str(value)
        str_value = "0" * (5 - len(str(value))) + str(value)
        # print(str_value)
        li2.append(str_value)
    li = li2
    while index <= max(li):
        for str_value in li:
            list_one_to_ten[int(str_value[-index])].append(str_value) ####这里可用数学方法，这样就不用因为out of index 去凑0
            #可以这样
            # digit = (value//(10**(index-1)))%10
            # list_one_to_ten[digit].append(value)

        # li.clear()
        # print(list_one_to_ten)
        li.clear()
        for small_list in list_one_to_ten:
            li += small_list
        ###这里将小表格合并成一个大表格：用list.extend(嵌套的小表格)
        # for small_list in list_one_to_ten:
        #     li.extend(small_list)
        for small_list in list_one_to_ten:
            small_list.clear()
        index += 1
    print(li)
    li3 = []
    for value in li:
        li3.append(int(value))
    print(li3)

li = [910,281,890,238,875,870,100]
p1 = redixsort(li)



