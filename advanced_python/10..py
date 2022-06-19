import os
import spacy
import pandas as pd
text = "I 'll do any notices announcing police officers"
def ner(sentence):
    list_ent = []
    nlp = spacy.load('en_core_web_md')
    doc = nlp(sentence)
    for s in list(doc.sents):
        for ent in s.ents:
            list_ent.append(ent.text)
    return len(list_ent)
print(ner(text))
# s_ner_number_list = []
# path  = "/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json_test/txt/CONVRSN_all_26_clean.txt"
# with open(path) as f:
#     s_list = f.read().split("\n")
# for s in s_list:
#     ner_number = ner(s)
#     s_ner_number_list.append(ner_number)
#
# new_path = path.replace("txt", "csv")
# df1 = pd.read_csv(new_path)
# df1["NER"] = s_ner_number_list
# df1.to_csv(new_path, index=False, sep=',')


s_ner_number_list = []
file_path = "/Users/zhoujie/Desktop/NONAC_all_7362_clean.txt"
print(file_path)
new_path = file_path.replace("txt", "csv")
with open(file_path) as f:
    s_list = f.read().split("\n")
for s in s_list:
    ner_number = ner(s)
    print(ner_number)
    s_ner_number_list.append(ner_number)
df1 = pd.read_csv(new_path)
df1["NER"] = s_ner_number_list
df1.to_csv(new_path, index=False, sep=',')
s_ner_number_list.clear()

