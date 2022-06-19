import spacy
import re
import os


def good_sent_pl(inpath, outpath):
    i = 0
    nlp = spacy.load('en_core_web_md')
    with open(inpath) as f:
        sent_list = f.read().split("\n")
    for sent in sent_list:
        doc = nlp(sent)
        # print(doc)
        i += 1
        print(i)
        token_dep_list = [token.dep_ for token in doc]
        # print(token_dep_list)
        if "ROOT" in token_dep_list:
            if str(doc[token_dep_list.index("ROOT")]) == doc[token_dep_list.index("ROOT")].lemma_:
                verb = str(doc[token_dep_list.index("ROOT")])
                sub_sent = "\n" + " ".join(token_dep_list[:token_dep_list.index("ROOT")])
                regex1 = """\nnsubj.+ prep det pobj.+"""
                # regex2 = """\n
                if re.findall(regex1,sub_sent):
                    print("sent",sent)
                    print("verb",verb)
                    print("pos_", sub_sent)
                # print(token_dep_list)
                    with open(outpath, "a+") as q:
                        q.write(sent + "\n")

# good_sent("/Users/zhoujie/Desktop/paper_project/Texts/clean_xml1.txt", "/Users/zhoujie/Desktop/paper_project/Texts/Good_Sent.txt")
good_sent_pl("/Users/zhoujie/Desktop/paper_project/XML_to_TXT_Sent/H5.txt","/Users/zhoujie/Desktop/paper_project/pl_H5.txt")


