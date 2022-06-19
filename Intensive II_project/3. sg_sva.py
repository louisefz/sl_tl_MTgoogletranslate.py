import spacy
import re
def good_sent_sg(inpath, outpath):
    i = 0
    nlp = spacy.load('en_core_web_sm')
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
            verb = str(doc[token_dep_list.index("ROOT")])
            regex_verb_sg = "[a-z]*s$"
            if re.findall(regex_verb_sg,verb):
                sub_sent = "\n" + " ".join(token_dep_list[:token_dep_list.index("ROOT")])
                regex1 = """\ndet.+ nsubj.+ prep.+ pobj.+"""
                # regex2 = """\n

                if re.findall(regex1,sub_sent):
                    print("sent",sent)
                    print("verb",verb)
                    print("pos_", sub_sent)
                # print(token_dep_list)
                    with open(outpath, "a+") as q:
                        q.write(sent + "\n")

# good_sent("/Users/zhoujie/Desktop/paper_project/Texts/clean_xml1.txt", "/Users/zhoujie/Desktop/paper_project/Texts/Good_Sent.txt")
good_sent_sg("/Users/zhoujie/Desktop/paper_project/Texts/H2.txt","/Users/zhoujie/Desktop/paper_project/Good_sent_autoH2.txt")
