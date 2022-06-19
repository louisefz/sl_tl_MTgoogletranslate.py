




def partition(li,left,right):
    tmp = li[left]  ###不是tmp = li[0], 有可能会切片slicing
    while left<right: ###当left = right的时候，大循环结束
        while left <right and li[right]>=tmp: #如果该式子成立，则right继续向前,当如果不写while
            right -= 1 ###则right往前移动，直到遇到li[right]<tmp的数，才能退出这个小循环
        li[left] = li[right]
        while left <right and li[right]>=tmp:
    li[left] = tmp  ####也可以是li[right] = tmp，因为此时right = left了


