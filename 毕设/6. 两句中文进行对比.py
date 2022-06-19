import os

path1 = "/Users/zhoujie/Desktop/LREC2020-ENZH-translation/"
path2 = "/Users/zhoujie/Desktop/HT_ZH/"
files1 = os.listdir(path1)
files2 = os.listdir(path2)


file_crp1 = []
MT_large1 = []
file_crp2 = []
HT_large2 = []
for file in files1:
    if os.path.splitext(file)[1] == ".crp":
        file_crp1.append(file)
file_crp1.sort()
# print(file_crp1)
for fc in file_crp1:
    with open(path1 + fc) as p:
        MT_st_text = p.read()  ####读取MT翻译的文章，包括en和汉(MT)
        line_list = MT_st_text.split("\n")
        new_list = [line_list[i:i+4]for i in range(0,len(line_list),4)]
        print(new_list)
        MT_large1.append(new_list)
# print(len(MT_large1))
# print(MT_large1[1])
for file in files2:
    file_crp2.append(file)
file_crp2.sort()
# print(file_crp2)
for f in file_crp2:
    with open(path2 + f) as q:
        HT_t_text = q.read()
        HT_t_list = HT_t_text.split("\n")
        # print(HT_t_list)
        HT_large2.append(HT_t_list)
print(HT_large2)
print()


###现在有MT_large1和HT_large2这两个列表
large3 = []
for index_out, mt in enumerate(MT_large1):  ###遍历整个文件夹中的每一个文件
    for index_in, m in enumerate(mt): ###遍历一个文件夹中的内容
        m.append(HT_large2[index_out][index_in])
        block = "\n".join(m)
        # print(block)
        large3.append(block)
input = "\n".join(large3)

with open(path2+"all_compare_chinese2MT_HT.crp", "w") as w:
    w.write(input)






















