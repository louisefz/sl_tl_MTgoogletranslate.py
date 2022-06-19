# 1. 将文件拼接在一起，做成csv
# 2. 将文件做成表格，找到root， nsubj,分成两列
# 3. 进行correction和modification:删除不符合要求的句子；修改句子，名词修改，动词修改
import os
import spacy
import xlwt
import pandas as pd

def sva(path):
    with open(path) as f:
        sent_list = f.read().split("\n")
        for sent in sent_list:
            with open("/Users/zhoujie/Desktop/paper_project/pl_sva_all.txt","a+") as q:
                q.write(sent+"\n")
# g = os.walk("/Users/zhoujie/Desktop/paper_project/pl_sva")
# for path, dir_list, file_list in g:
#     for file in file_list:
#         file_path = os.path.join(path, file)
#         print(file_path)
#         sva(file_path)


# 将txt转化成csv
def txt_to_xlsx(path):
    new_path = path.replace(".txt",".xlsx")
    f = open(path)
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
    x = 0
    while True:
        # 按行循环，读取文本文件
        line = f.readline()
        if not line:
            break  # 如果没有内容，则退出循环
        for i in range(len(line.split('\t'))):
            item = line.split('\t')[i]
            sheet.write(x, i, item)  # x单元格经度，i 单元格纬度
        x += 1  # excel另起一行
    f.close()
    xls.save(new_path)  # 保存xls文件

# txt_to_xlsx("/Users/zhoujie/Desktop/paper_project/pl_sva_all.txt")
# txt_to_xlsx("/Users/zhoujie/Desktop/paper_project/sg_sva_all.txt")

####找到csv>>sentence中的nsubj和root
def nsubj(txt_path,csv_path):
    nsubj_list = []
    nsubj_sent_list = []
    root_list = []
    nlp = spacy.load('en_core_web_md')
    f = open(txt_path)
    sent_list = f.read().split("\n")
    for sent in sent_list:
        doc = nlp(sent)
        token_dep_list = [token.dep_ for token in doc]
        if "ROOT" in token_dep_list:
            for token in doc[:token_dep_list.index("ROOT")+1]:
                if token.dep_ == "nsubj":
                    nsubj_sent_list.append(str(token))
                    # print(nsubj)
                elif token.dep_ =="ROOT":
                    root = token
                    # print(root)
                    root_list.append(root)
            nsubj = " ".join(nsubj_sent_list)
            nsubj_list.append(nsubj)
            nsubj_sent_list.clear()
        else:
            nsubj_list.append(" ")
            root_list.append(" ")
    print(len(root_list))
    print(len(nsubj_list))
    df1 = pd.read_csv(csv_path)
    df1["root"] = root_list
    df1.to_csv(csv_path, index=False, sep=',')
    df1["nsubj"] = nsubj_list
    df1.to_csv(csv_path, index=False, sep=',')

nsubj("/Users/zhoujie/Desktop/paper_project/pl_sva_all.txt","/Users/zhoujie/Desktop/paper_project/pl_sva_all_1.csv")
nsubj("/Users/zhoujie/Desktop/paper_project/sg_sva_all.txt","/Users/zhoujie/Desktop/paper_project/sg_sva_all_1.csv")


