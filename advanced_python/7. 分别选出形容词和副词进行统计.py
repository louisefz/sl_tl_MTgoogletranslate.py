###1. 每个句子的形容词数量/句子总token的数量（不算标点符号）
###2. 每个句子的副词数量/句子总token的数量（不算标点符号）
###3. 用CVS存起来
import os
import re
import pandas as pd
# g = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json_test")
# for path,dir_list,file_list in g:
#     for file in file_list:
#         file_path = os.path.join(path, file)
#         print(file_path)
#         with open(file_path) as f:
#             js_text = f.read()
#             s_list = js_text.split("\n")
#             for s in s_list:


###1.  每个句子中Adj.的数量
###2. ，每个句子中Adv.的数量

def adj(path):
    regex1 = "ADJ"
    list_adj_number = []
    with open(path) as f:
        js_s_list = f.read().split("\n")
        for js_s in js_s_list:
            adj_number = len(re.findall(regex1,js_s))
            list_adj_number.append(adj_number)
        return list_adj_number
adj("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json_test/JSON/CONVRSN_all_26_clean.json")


def adv(path):
    regex1 = "ADV"
    list_adj_number = []
    with open(path) as f:
        js_s_list = f.read().split("\n")
        for js_s in js_s_list:
            adj_number = len(re.findall(regex1,js_s))
            list_adj_number.append(adj_number)
        return list_adj_number
adv("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json_test/JSON/CONVRSN_all_26_clean.json")


####还需要统计均值%除以句子token总数

g = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_JSON_test/json")
s_ner_number_list = []
for path,dir_list,file_list in g:
    for file in file_list:
        file_path = os.path.join(path, file)
        print(file_path)
        new_path = file_path.replace("json", "csv")
        adj_number_list = adj(file_path)
        adv_number_list = adv(file_path)
        df1 = pd.read_csv(new_path)
        df1["Adj"] = adj_number_list
        df1.to_csv(new_path, index=False, sep=',')
        df1 = pd.read_csv(new_path)
        df1["Adv"] = adv_number_list
        df1.to_csv(new_path, index=False, sep=',')





