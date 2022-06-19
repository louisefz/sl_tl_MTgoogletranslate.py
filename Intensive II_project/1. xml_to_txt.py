import os
import re
from xml.dom.minidom import parseString
###1. 选取一些句子
#运用spacy的依存关系，找到root.index>3的句子
#然后用regex过滤不符合要求的句子，如root是情态动词，
g = os.walk("/Users/zhoujie/Desktop/paper_project/TXT")
for path, dir_list, file_list in g:
    for file in file_list:
        file_path = os.path.join(path, file)
        new_path = file_path.replace(".txt",".xml")
        # with open(file_path, 'a+', encoding='utf-8') as test:
        #     test.truncate(0)
        # os.rename(file_path,new_path)




def sent_find(large_path):
    g = os.walk(large_path)
    for path, dir_list, file_list in g:
        for file in file_list:
            file_path = os.path.join(path, file)
            print(file_path)
            # new_path = file_path.replace("Texts", "CLEAN_XML")
            with open(file_path) as q:
                xml_sent_list = q.read().split("\n")
                # print(xml_sent_list)
            for xml_sent in xml_sent_list:
                regex = "<s n="
                if re.findall(regex,xml_sent):
                    with open("/Users/zhoujie/Desktop/paper_project/Texts/K.xml", "a+") as p:
                        p.write(xml_sent + "\n")
# sent_find("/Users/zhoujie/Desktop/paper_project/Texts/K")


def clean_xml(xml_sent):
    new_xml_sent = re.sub(r"</s>.+", r"</s>",xml_sent)
    return new_xml_sent


def xml_to_txt(xml_sent):

    dom = parseString(xml_sent)
    ss = dom.getElementsByTagName('s')
    for s in ss:
        ww = s.getElementsByTagName('w')
        txt_sent = " ".join([w.firstChild.data for w in ww]) + "\n"
        new_txt_sent = txt_sent.replace("  "," ")
    return new_txt_sent

def parsing_able(path, outpath):
    with open(path) as g:
        xml_sent_list = g.read().split("\n")
    for xml_sent in xml_sent_list[:-1]:
        new_xml_sent = clean_xml(xml_sent)
        txt_sent = xml_to_txt(new_xml_sent)
        with open(outpath, "a+") as h:
            h.write(txt_sent)
parsing_able("/Users/zhoujie/Desktop/paper_project/Texts/K.xml", "/Users/zhoujie/Desktop/paper_project/Texts/K1.txt")

