# 算法步骤
# 设置几个数组作为空桶。
# 从左到右遍历待排序序列，把每个元素都放到对应的桶中
# 对每个不是空的桶进行排序。
# 依次取出所有桶中的元素放回原序列


def bucketsort(li,n=4):
    max_number = max(li)
    min_number = min(li)
    discrepancy = (max_number - min_number)/4
    bucket = [[] for _ in range(n)]
    for value in li:
        if value >= min_number and value <= (max_number+3*min_number)/4:

            for index, subvalue in enumerate(bucket[0]):
                if bucket[0][index]>bucket[0][index-1]:
                    bucket[0].append(value)
                else:
        elif value >= (max_number+3*min_number)/4 and value <= (2*max_number + 2*min_number) / 4:
            bucket[1].append(value)
        elif value >= (2*max_number + 2*min_number) / 4 and value <= (3 * max_number + 1 * min_number) / 4:
            bucket[2].append(value)
        elif value >= (3 * max_number + 1 * min_number) / 4 and value <= max_number:
            bucket[3].append(value)

        ####这种方法if elif方法很笨，如果n很大，则不能这么分
        ####在append之后进行排序时，可以用冒泡排序，也可以用sorted()去对每个桶进行排序,也可以调用其他排序的算法函数






 def bucketsort(li,n):
     max_number = max()
     min_number = min()
     bucket = [[] for _ in range(n)]
     bucket_timestep = (max_number-min_number)//n
     for value in li:
         bucket_index = (value-min_number)//bucket_timestep
         bucket[bucket_index].append(value)
         for index in range(len(bucket[bucket_index])):
             if bucket[bucket_index][index] < bucket[bucket_index][index-1]:
                 bucket[bucket_index][index],bucket[bucket_index][index-1] = bucket[bucket_index][index-1],bucket[bucket_index][index] ###交换位置
            else:
                break #如果是大于等于，则退出冒泡排序
                ###当然，这里的排序，也可以用sorted（）或者其他任何一种排序方式
     li.clear()
     for s_bucket in bucket:
        li.extend(s_bucket)
     print(li)










