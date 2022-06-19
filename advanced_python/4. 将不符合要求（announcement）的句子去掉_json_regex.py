import re
import json
import os
regex = '''"@hw": "announce", "@pos": "VERB"|"@hw": "declare", "@pos": "VERB"'''
with open("/Users/zhoujie/Desktop/ACPROSE_all_675_test.json") as f:
    text_js = f.read()
    js_list = text_js.split("\n")
for js in js_list:
    if re.findall(regex,js):
        print(js)

def target_word_verb(file_path):
    regex1 = '''"@hw": "announce", "@pos": "VERB"|"@hw": "declare", "@pos": "VERB"'''
    regex2 = file_path
    new_path = regex2.replace(".","_clean.")
    with open(file_path) as f:
        text_js = f.read()
    js_list = text_js.split("\n")
    for js in js_list:
        if re.findall(regex1, js):
            with open(new_path,"a+") as q:
                q.write(js+"\n")
# target_word_verb("/Users/zhoujie/Desktop/ACPROSE_all_675_test.json")
# g = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data")
# for path,dir_list,file_list in g:
#     for file_name in file_list:
#         file_path = os.path.join(path, file_name)
#         target_word_verb(file_path)

def declare_announce_number(file_path):
    count1 = 0
    count2 = 0
    regex1 = '''"@hw": "announce", "@pos": "VERB"'''
    regex2 = '''"@hw": "declare", "@pos": "VERB"'''
    with open(file_path) as f:
        text_js = f.read()
    js_list = text_js.split("\n")
    for js in js_list:
        if re.findall(regex1, js):
            count1 += 1
        elif re.findall(regex2, js):
            count2 += 1
    return count1, count2


# print(declare_announce_number("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json/ACPROSE_all_675_clean.json"))
g = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json")
for path,dir_list,file_list in g:
    for file_name in file_list:
        file_path = os.path.join(path, file_name)
        print(declare_announce_number(file_path))

