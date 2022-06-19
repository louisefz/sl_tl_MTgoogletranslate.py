import os
import shutil
from xml.dom.minidom import parseString
with open("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json_test/XML/UNPUB_all_239_clean.xml") as f:
    xml_text = f.read()
xml_list = xml_text.split("\n")
i = 1
for x in xml_list:
    dom = parseString(x)
    ss = dom.getElementsByTagName('s')
    s_list = []
    for s in ss:
        ww = s.getElementsByTagName('w')
        # print(ww)
        # print([w.firstChild.data for w in ww])
        list_s = " ".join([w.firstChild.data for w in ww])
        print(i,list_s)
        i += 1

def xml_to_txt(path):
    txt_path = path.replace(".xml", ".txt")
    with open(path) as f:
        xml_list = f.read().split("\n")
        for xml in xml_list:
            dom = parseString(xml)
            ss = dom.getElementsByTagName('s')
            for s in ss:
                ww = s.getElementsByTagName('w')
                s_token = " ".join([w.firstChild.data for w in ww]) + "\n"
                with open(txt_path,"a+") as q:
                    q.write(s_token)
g = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json_test/XML")
for path, dir_list, file_list in g:
    for file in file_list:
        file_path = os.path.join(path, file)
        xml_to_txt(file_path)
