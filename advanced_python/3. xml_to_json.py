
import xmltodict, json
import os
import re
g = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/Texts")
for path,dir_list,file_list in g:
    for file_name in file_list:
        file_path = os.path.join(path, file_name)
with open("/Users/zhoujie/Desktop/ACPROSE_all_675_test.xml") as f:
    text = f.read()
    text_list = text.split("\n")
i = 1
for s in text_list:
    o = xmltodict.parse(s)
    print(i, ":", json.dumps(o))
    i += 1



def xml_to_js(file_path):
    i = 1
    regex = file_path
    new_path = regex.replace("xml","json")
    with open(file_path) as f:
        text = f.read()
    text_list = text.split("\n")
    for s in text_list:
        o = xmltodict.parse(s)
        js = json.dumps(o) + "\n"
        print(i, js)
        i +=1
        with open(new_path,"a+") as q:
            q.write(js)
# xml_to_js("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/UNPUB_all_320.xml")
g = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data")
for path,dir_list,file_list in g:
    for file_name in file_list:
        file_path = os.path.join(path, file_name)
        xml_to_js(file_path)

