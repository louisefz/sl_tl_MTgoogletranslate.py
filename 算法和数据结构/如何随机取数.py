'''
import random
li = list(range(10000))
random.shuffle(li)
print(li)
'''
dict = {('<s>', '['): 1, ('[', 'emma'): 1, ('emma', 'by'): 1, ('by', 'jane'): 1, ('jane', 'austen'): 1, ('austen', '1816'): 1}

for x,y in dict.items():
    print(x[:-1])
