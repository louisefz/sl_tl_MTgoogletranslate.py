# 1. 需要对文本进行分类
# 2. 需要提取有declare/announce的句子
# 3. 再筛选出有pos = "VERB"的句子
# 4. 对筛选出来的句子转化成txt的格式
# 5. 对txt格式的句子进行特征统计，即对input的x进行统计

###1. 对xml文本按照genre进行分类
import os
import shutil
import xml.dom.minidom

# g = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/Texts")
# for path,dir_list,file_list in g:
#     for file_name in file_list:
#         file_path = os.path.join(path, file_name)
        # print(file_path)
        # dom = xml.dom.minidom.parse(file_path)
        # root = dom.documentElement
        # if root.getElementsByTagName('wtext'):
        #     type1 = root.getElementsByTagName('wtext')[0].getAttribute("type")
        #     if type1 == "ACPROSE":
        #         shutil.move(file_path, "/Users/zhoujie/Desktop/logistic_reg_project/genre/wtext/ACPROSE")
        #     elif type1 == "FICTION":
        #         shutil.move(file_path, "/Users/zhoujie/Desktop/logistic_reg_project/genre/wtext/FICTION")
        #     elif type1 == "NEWS":
        #         shutil.move(file_path, "/Users/zhoujie/Desktop/logistic_reg_project/genre/wtext/NEWS")
        #     elif type1 == "NONAC":
        #         shutil.move(file_path, "/Users/zhoujie/Desktop/logistic_reg_project/genre/wtext/NONAC")
        #     elif type1 == "OTHERPUB":
        #         shutil.move(file_path, "/Users/zhoujie/Desktop/logistic_reg_project/genre/wtext/OTHERPUB")
        #     elif type1 == "UNPUB":
        #         shutil.move(file_path, "/Users/zhoujie/Desktop/logistic_reg_project/genre/wtext/UNPUB")
        # elif root.getElementsByTagName('stext'):
        #     type2 = root.getElementsByTagName('stext')[0].getAttribute("type")
        #     if type2 == "CONVRSN":
        #         shutil.move(file_path, "/Users/zhoujie/Desktop/logistic_reg_project/genre/stext/CONVRSN")
        #     elif type2 == "OTHERSP":
        #         shutil.move(file_path, "/Users/zhoujie/Desktop/logistic_reg_project/genre/stext/OTHERSP")
        # else:
        #     shutil.move(file_path, "/Users/zhoujie/Desktop/logistic_reg_project/genre/other")



### 需要提取有declare/announce的句子
# h = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/genre")
# for path,dir_list,file_list in h:
#     for file_name in file_list:
#         file_path = os.path.join(path, file_name)
#         # print(file_path)
#         dom = xml.dom.minidom.parse(file_path)
#         ss = dom.getElementsByTagName('u')
#         for s in ss:
#             print(s)



# dom = xml.dom.minidom.parse("/Users/zhoujie/Desktop/logistic_reg_project/genre/wtext/ACPROSE/CGA.xml")
# ss = dom.getElementsByTagName('s')
# s_list = []
# for s in ss:
#     ww = s.getElementsByTagName('w')
#     list_s = " ".join([w.firstChild.data for w in ww])
#     # print("sentence:",list_s)
#     for w in list_s.split(" "):
#         if w == "give":
#             break
#         s_list.append(list_s)
# print(len(s_list))

import re
# text = ["I declare it today", "I announced that", "she is announcement right"]
regex = r"declar(e|i)|announc(e|i)"
# for s in text:
#     if re.findall(regex, s):
#         print(s)
# def target_sentence_new_file(file):
#     list_give = []
#     g = os.walk(file)
#     for path, dir_list, file_list in g:
#         for file_name in file_list:
#             file_path = os.path.join(path, file_name)
#             with open(file_path) as h:
#                 text_xml = h.read()
#                 for s in text_xml.split("\n")[2:-1]:
#                     if re.findall(regex, s):
#                         list_give.append(s)
#             with open(file_path, "w") as p:
#                 p.write("\n".join(list_give))
#             list_give.clear()
list_give = []
g = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/genre_handlable")
# for path,dir_list,file_list in g:
#     for file_name in file_list:
#         file_path = os.path.join(path, file_name)
#         print(file_path)
#         with open(file_path) as h:
#             text_xml = h.read()
#             for s in text_xml.split("\n")[2:-1]:
#                 if re.findall(regex, s):
#                     list_give.append(s)
#         with open(file_path, "w") as p:
#             p.write("\n".join(list_give))
#         list_give.clear()


# def big_new_file(file):
#     for path, dir_list, file_list in file:
#         file_path = os.path.join(path, file_name)
#         with open(file_path) as t:
#             text_xml = t.read()
#         with open(path + "/all.xml", "a+") as c:
#             c.write(text_xml)

for path,dir_list,file_list in g:
    for file_name in file_list:
        file_path = os.path.join(path, file_name)
        # print(file_path)
        with open(file_path) as t:
            text_xml = t.read()
        with open(path + "/all_big.xml", "a+") as c:
            c.write(text_xml)



# list_give = []
# with open("/Users/zhoujie/Desktop/logistic_reg_project/genre_handlable/wtext/ACPROSE/CGA.xml") as f:
#     text = f.read()
#     s_list = text.split("\n")[2:-1]
#     for s in s_list:
#         if re.findall(regex, s):
#             print(s)
#             list_give.append(s)
# with open("/Users/zhoujie/Desktop/logistic_reg_project/CGA.xml", "w") as q:
#     q.write("\n".join(list_give))

##把每个句子变成字典形式，用json存起来





#解析 xml文本
"""
<?xml version="1.0" encoding="utf-8"?>
<catalog>
       <maxid>4</maxid>
       <login username="pytest" passwd='123456'>
            　　<caption>Python</caption>
             <item id="4">
                    <caption>测试</caption>
            </item>
    </login>
    <item id="2">
            <caption>Zope</caption>
    </item>
</catalog>
"""


import xml.dom.minidom

#####
# dom = xml.dom.minidom.parse('/Users/zhoujie/Desktop/logistic_reg_project/test.xml')
# root = dom.documentElement
# bb = root.getElementsByTagName('maxid')
# b= bb[0]
# print(b.nodeName)
# bb = root.getElementsByTagName('caption')
# b= bb[2] #有3个<caption>，打印的是第三个<caption>
# print(b.nodeName)
#
# #获取pos = "VERB"
# itemlist = root.getElementsByTagName('login')
# item = itemlist[0]
# un=item.getAttribute("username")
# print(un)
# pd=item.getAttribute("passwd")
# print(pd)

####获取标签之间的正文部分（所有正文部分），如果c.firstChild.data  == announce or declare, 则print<s>
# cc=dom.getElementsByTagName('caption')
# for c in cc:
#     print(c.firstChild.data)