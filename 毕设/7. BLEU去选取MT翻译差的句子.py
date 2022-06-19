# BLEU编程实现的主要任务是对候选翻译和参考翻译的n元组进行比较，并计算相匹配的个数。
# 匹配个数与单词的位置无关。匹配个数越多，表明候选翻译的质量就越好。

##试一试n—gram，我觉得主要是用unigram一元进行衡量

from nltk.translate.bleu_score import sentence_bleu
# candidate = ['印度', '国防部', '发言人', '说', ':', '“', '即将', '举行', '的', '演习', '旨在', '进一步', '提升', '印', '美', '之间', '的', '军事', '合作', '。', '”']
# reference = [['印度', '国防部', '发言人', '说', ':“即将', '举行', '的', '演习', '旨在', '进一步', '提升', '印度', '与', '美国', '的', '军事', '合作', '关系。”']]
# score = sentence_bleu(reference, candidate)
# print(score)

def bleu_score(candidate, reference):
    score = sentence_bleu(reference, candidate)
    return score

def split(sentence):
    list_text = sentence.split(" ")
    return list_text
split("印度 国防部 发言人 说 :“即将 举行 的 演习 旨在 进一步 提升 印度 与 美国 的 军事 合作 关系。”")


with open("/Users/zhoujie/Desktop/HT_ZH/all_compare_chinese2MT_HT_test.crp") as t:
    compare_text = t.read()

compare_text_list = compare_text.split("\n")
four_line_list = [compare_text_list[i:i+5] for i in range(0,len(compare_text_list),5)]
# print(four_line_list)

list_good_translate = []
for unit in four_line_list:
    candi_g = unit[-3]
    candi_d = unit[-2]
    ref = [unit[-1]]
    score_g = bleu_score(candi_g,ref)
    score_d = bleu_score(candi_d,ref)
    print(score_g)
    print(score_d)
    print("-"*20)
    unit.append(str(score_g))
    unit.append(str(score_d))
    list_good_translate.append("\n".join(unit))

with open("/Users/zhoujie/Desktop/HT_ZH/all_compare_chinese2MT_HT_test.crp","w") as y:
    y.write("\n".join(list_good_translate))





