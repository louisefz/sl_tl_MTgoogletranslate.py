'''
import os
word1 = 0
with open("/Users/zhoujie/Downloads/ota_20.500.12024_2554/download/Texts/A/A0/A00.xml") as f:
    list1 = f.read().split()
    print(list1)
    for words in list1:
        if "her" in list1:
            word1 += 1
print(word1)
'''
import os
txt1 = []
#遍历文件夹
def iter_files(rootDir):
    #遍历根目录
    for path in os.path.isfile():
        for subpath in path:
            with open(subpath) as d:
                txt1.append(d.read().split())
                with open("/Users/zhoujie/Desktop/data_2", "w") as f:
                    print(f.write(txt1))
iter_files('/Users/zhoujie/Downloads/ota_20.500.12024_2554/download/Texts')













