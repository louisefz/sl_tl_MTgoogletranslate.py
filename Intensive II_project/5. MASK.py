# 1. 将句子mask
#具体步骤：
# A. 将用第二列的动词遍历整个句子，找到句子中的动词，然后[MASK]
#
import csv
import spacy


# csv_reader = csv.reader(open("/Users/zhoujie/Desktop/paper_project/sg_sva_all.csv"))
# for line in csv_reader:
#     token_list = line[-1].replace('\n','').split(" ")
#     if "[MASK]" in token_list:
#         # print(line)
#         line.append(line[-1])
#         # with open("/Users/zhoujie/Desktop/paper_project/sg_sva_mask1.csv","a+", newline='') as f:
#         #     writer = csv.writer(f)
#         #     writer.writerow(line)
#     else:
#         if line[1] in token_list:
#             mask_sent = line[-1].replace(" "+ line[1] +" "," [MASK] ")
#             line.append(mask_sent)
                # print(mask_sent)
        # print(line)
        # with open("/Users/zhoujie/Desktop/paper_project/sg_sva_mask2.csv","a+", newline='') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(line)

        # if line[1] not in token_list:
        #     print(line)


####将csv1第三列中的[MASK]换成动词
# csv_reader = csv.reader(open("/Users/zhoujie/Desktop/paper_project/sg_sva_mask1.csv"))
# for line in csv_reader:
#     unmasked_sent = line[-2].replace('[MASK]', line[1])
#     line[-2] = unmasked_sent
    # with open("/Users/zhoujie/Desktop/paper_project/sg_sva_mask3.csv", "a+", newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(line)


###将csv2中的多个[MASK]句子挑出来，手动筛选
# csv_reader = csv.reader(open("/Users/zhoujie/Desktop/paper_project/sg_sva_mask2.csv"))
# i = 0
# for line in csv_reader:
#     mask_sent_token_list = line[-1].split(" ")
#     if mask_sent_token_list.count("[MASK]") > 1:
#         with open("/Users/zhoujie/Desktop/paper_project/sg_sva_mask4.csv", "a+", newline='') as f:
#             writer = csv.writer(f)
#             writer.writerow(line)
#     else:
#         with open("/Users/zhoujie/Desktop/paper_project/sg_sva_mask5.csv", "a+", newline='') as f:
#             writer = csv.writer(f)
#             writer.writerow(line)





###找到wrong prediction ROOT
def wrong_root(word):
    nlp = spacy.load('en_core_web_md')
    token = nlp(word)
    for t in token:
        return t.lemma_


# csv_reader = csv.reader(open("/Users/zhoujie/Desktop/paper_project/sg_sva_mask3_good.csv"))
# for line in csv_reader:
#     if line[1] == "is":
#         wrong_predict = "are"
#         line.append(wrong_predict)
#     elif line[1] == "was":
#         wrong_predict = "were"
#         line.append(wrong_predict)
#     else:
#         wrong_predict = wrong_root(line[1])
#         line.append(wrong_predict)
    # with open("/Users/zhoujie/Desktop/paper_project/sg_sva_mask_wrong_root.csv", "a+", newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(line)


csv_reader = csv.reader(open("/Users/zhoujie/Desktop/paper_project/sg_sva_mask_wrong_root.csv"))
for line in csv_reader:
    token_list = line[-1].replace("\n","").split(" ")
    if "[MASK]" not in token_list:
        print(line)