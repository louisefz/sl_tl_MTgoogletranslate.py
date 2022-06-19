# 不停地去执行
# while True:
#     print(1)
# print(x) ###被黄色hilight的代码是不能被执行的，因为永远执行不到，因为上面的是无限循环


###
number  = 0
while number <10:
    number += 1
    if number == 5:
        continue  ####如果continue下有有必要执行的任务，则会跳过；如果没有有必要执行的任务，则不会跳过。
    print(number)

#####pass语句的用法： 如果写了一段代码，但是接下来的代码语句没有想好，则可以用pass；之后写的代码程序不会报错
if number >10:
    pass
print(13414)


for i in range(10):
    if i<=5:
        print("*" * i)
    else:
        print("*" * (10-i))

j = 1
for i in range(1,10):
    x = i * j
    print(str(i) + "*" + str(j) + "=", x)
    

