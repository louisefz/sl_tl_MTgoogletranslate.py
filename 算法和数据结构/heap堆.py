###堆排序的实现
# （1）用向下排序
# （2）建堆
# （3）把堆顶值（省长）依次调出来进行排序

# （1）用向下排序
def sift(li,low,high):
    """

    :param li: 列表
    :param low: 堆的根节点的位置  指的是下表，而不是元素的数值
    :param high: 堆的最后一个元素的位置 ：作用：因为是父亲找孩子，从上往下找，high这个下表可以帮助我们是否看我你们的*2+1是否超过了high的值
    :return:
    """
    i = low
    j = 2*i + 1
    tmp = li[i]
    while j <= high:
        if j+1 <= high and li[j+1] >li[j]: ###需要保证j+1也要小于high 且a and b和b and a不一样；这样的顺序会报错li[j+1] >li[j] and j+1 <= high，调换一下就可以了
            j = j+1
        else:
            j = j
        if li[j] > tmp:  ###这个if会一直循环
            #j = i 不能这么写
            li[i] = li[j] ####li[i] = li[j]或者li[j] = li[i]都可以完成替换
            i = j
            j = 2*i+1  ###看下一层j
        else:
            li[i] = tmp ####i始终代表的是位置，tmp则代表的是初始i位置的值
            break
    else:
        li[i] = tmp


#print([i for i in range(10)])

# （2）建堆：找到最下层的父节点，依次从右到左，从下到上找到父节点，然后进行排序
def heaps_sort(li):
    n = len(li)
    for i in range((n-2)//2,-1,-1): ##从下往上，要找到最下面的一个父节点所在的位置为:其最下方的子节点为n-1,因此父节点为(n-1-1)//2；由于是倒序查找，找到下表位置步长为-1，知道找到下表为0的数字，如果写0，则不包括0位置的数，因此要写到-1.
        sift(li,i,n-1)  ####这里的high值是n-1而不是算i的子节点，直接用整个树的high值就可以了。不会出错的，死记！！！！
    #print(li)
# （3）把堆顶值（省长）依次调出来进行排序
    for i in range(n-1,-1,-1): ###从high开始进行循环，这样从high到low每个值都会变成high
        li[0],li[i] = li[i], li[0] ###将high和low的值进行对调 因为在low位置的最大值为了节省空间，不必再占用新的储存空间，因此可以直接存在之前的high的位置
        ###由于现在high的位置也就是i储存了low的值，因此，新的high值应该是i-1
        ####接下来需要对新的树进行堆的排序
        sift(li,0,i-1)
    print(li)

####时间复杂度：
# （1）堆排序的时间复杂度：一个列表中有n个元素，则根据二叉树的原则，层数有logn层，而堆排序的最大经过树的深度，因此是logn
# （2）（2）中找到父节点的循环为n/2，因此时间复杂度为n，（2）中的堆排序时间复杂度为logn，因此（2）的时间复杂度为nlogn
# （3）同理，（3）中的时间复杂度为nlogn
# 由于（2）和（3）是两个for循环，没有嵌套关系，因此整个heaps_sort(li)函数的时间复杂度为nlogn


import random
li = [i for i in range(100)]  ###range(a,b,c)函数代表下标：a为起始值（被包括），b为终点值（不被包括），c为步长
random.shuffle(li)
heaps_sort(li)


####堆排序中，python中有内置的模块heapq
import heapq
###建小根堆（升序）：
li = list(range(100))
random.shuffle(li)
heapq.heapify(li)
print(li)
####小根堆排序
heapq.heappop(li)
print(li)










