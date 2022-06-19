# 1. subject_verb distance
# 2. number of attractors
# 3. the distance from non-nsubj to verb
# 4. 句式： 是否有which/that，
# 5. root之后的动词或者名词数量
# 6. root之前的token数量
# 7. 每个句子token的总数
# 8. root之前verb的数量以及单复数情况
import spacy
import csv
import shutil
import pandas as pd

# 1. subject_verb distance
# 7. 每个句子token的总数
def svd(sent,nsubj,root):
    token_list = sent.split(" ")
    print(token_list)
    len_sent = len(token_list)
    nsubj_index = token_list.index(nsubj)
    root_index = token_list.index(root)
    sv_distance = abs(root_index - nsubj_index)
    return len_sent,sv_distance

# 2. number of attractors
# 4. root前有几个动词
# 6. root之前的token数量
def attractor(sent,nsubj,root):
    i_all = 0
    j = 0
    noun_list = []
    nlp = spacy.load("en_core_web_md")
    sent_doc = nlp(sent)
    token_list = sent.split(" ")
    print(token_list)
    mask_index = token_list.index(root)
    len_before_root = len(token_list[:mask_index])
    for token in sent_doc[:mask_index]:
        if token.pos_ == "NOUN" and token.text != nsubj:
            i_all += 1
            noun_list.append(token)
        elif token.pos_ == "VERB":
            j += 1
    return i_all,j,len_before_root,mask_index,noun_list

# 3. the distance from non-nsubj to verb
def non_nsubj_to_verb(sent, nsubj,root):
    i = 0
    pl_noun_list = []
    token_list = sent.split(" ")
    _,_,_,mask_index,noun_list = attractor(sent, nsubj,root)
    for noun in noun_list:
        if noun.lemma_ != noun.text:
            pl_noun_list.append(noun.text)
            i += 1
        else:
            i = i

    if pl_noun_list == []:
        nearest_noun_root_distance = "none"
        return i, nearest_noun_root_distance
    else:
        nearest_noun_index = token_list.index(pl_noun_list[-1])
        nearest_noun_root_distance = abs(mask_index - nearest_noun_index)
        return i, nearest_noun_root_distance

def append_list(string,line_list):
    line_list.append(string)
    return line_list



csv_reader = csv.reader(open("/Users/zhoujie/Desktop/1_sg_bert.csv"))
for line in csv_reader:
    len_sent, sv_distance = svd(line[4].replace("\n",""),line[0].strip(),"[MASK]")
    i_all, j, len_before_root, _, noun_list = attractor(line[4].replace("\n",""),line[0].strip(),'[MASK]')
    i,nearest_noun_root_distance = non_nsubj_to_verb(line[4].replace("\n",""), line[0].strip(),"[MASK]")
    para = [len_sent,sv_distance,i_all,j,len_before_root,i,nearest_noun_root_distance]
    for p in para:
        line = append_list(p,line)
    print(line)
    with open("/Users/zhoujie/Desktop/paper_project/sg_sva_mask_full_para.csv", "a+") as f:
        writer = csv.writer(f)
        writer.writerow(line)

###duplicate csv file
frame=pd.read_csv('/Users/zhoujie/Desktop/paper_project/sg_sva_mask_full_para.csv',engine='python')
data = frame.drop_duplicates(subset=None, keep='first', inplace=False)
data.to_csv('/Users/zhoujie/Desktop/paper_project/sg_sva_mask_full_para_duplicate.csv', encoding='utf8')








