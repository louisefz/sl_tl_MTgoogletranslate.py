list1 = [0,1,2,3,46,56,90,100]
print(list1[0:7])
print(list1[0:8])

def sort(li,low,mid,high):
    i = low
    j = mid+1
    ltmp =[]
    while i<=mid and j<=high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i+=1
        else:
            ltmp.append(li[j])
            j+=1
    while i<=mid:
        ltmp.append(li[i])
        i+=1
    while j<=mid:
        ltmp.append(li[j])
        j+=1
    li[low:high+1] = ltmp

li = list1 = [46,56,90,100,0,1,2,3]
sort(li,0,3,7)
print(li)

import random
li = list(range(100))
random.shuffle(li)
print()





