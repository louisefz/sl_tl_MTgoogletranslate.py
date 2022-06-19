import csv
import os
import re
import pandas as pd
g = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json_test")


# for path,dir_list,file_list in g:
#     for file in file_list:
#         file_path = os.path.join(path, file)
#         regex2 = file_path
#         new_path = regex2.replace(".json", ".csv")
#         print(new_path)
#         with open(new_path, "w")as f:
#             writer = csv.writer(f)
#             writer.writerow(["Genre", "Sentiment", "NER", "No./Tokens", "Ave.Len/ Token", "Adj.%", "Adv.%"])



###1. 将target word（declare/announce）存入CSV中
###2. 将Genre存入CSV 中
g = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json_test/JSON")
regex1 = '''announce|declare'''
list_tw = []
list_genre = []
i = 0
for path,dir_list,file_list in g:
    for file in file_list:
        file_path = os.path.join(path, file)
        regex2 = file_path
        csv_path = file_path.replace(".json",".csv")
        regex3 = '''ACPROSE|NEWS|OTHERSP|OTHERPUB|NONAC|FICTION|UNPUB|CONVRSN'''
        genre_name = " ".join(re.findall(regex3, regex2))
        # print(genre_name)
        list_genre.append(genre_name)
        with open(file_path) as q:
            js_sent = q.read()
            js_sent_list = js_sent.split("\n")
            for s in js_sent_list:
                i += 1
                target_word = re.findall(regex1,s)
                # print(target_word[0])
                list_tw.append(target_word[0])
            dataframe = pd.DataFrame({'target_word': list_tw, 'genre': list_genre * i})
            dataframe.to_csv(csv_path, index=False, sep=',')
        i = 0
        list_tw.clear()
        list_genre.clear()










####删除了既有declare又有announce的句子
# with open("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json_test/UNPUB_all_239_clean.json") as q:
#     regex1 = '''"announce"|"declare"'''
#     regex3 = '''"announce" "declare"'''
#     js_sent = q.read()
#     js_sent_list = js_sent.split("\n")
#     for s in js_sent_list:
#         target_word = re.findall(regex1,s)
#         # print(target_word,s)
#         if re.findall(regex3," ".join(target_word)):
#             print(" ".join(target_word), s)


