import spacy
import csv
def nsubj(sent):
    noun_list = []
    nlp = spacy.load("en_core_web_md")
    doc = nlp(sent)
    token_list = sent.split(" ")
    mask_index = token_list.index("[MASK]")
    for token in doc[:mask_index]:
        if token.pos_ == "NOUN":
            if token.lemma_ != token.text:
                noun_list.append(token.text)
    if noun_list == []:
        pass
    else:
        nsubj = noun_list[0]
        return nsubj

csv_reader = csv.reader(open("/Users/zhoujie/Desktop/lgd_dataset_10000_pl.csv"))
for line in csv_reader:
    subject = nsubj(line[-1])
    line[0] = subject
    with open("/Users/zhoujie/Desktop/lgd_dataset_10000_pl_good.csv","a+") as f:
        writer = csv.writer(f)
        writer.writerow(line)



csv_reader = csv.reader(open("/Users/zhoujie/Desktop/pl_rest_subject_good_first_half.csv"))
for line in csv_reader:
    token_list = line[-2].split(" ")
    number_occurrence = token_list.count(line[0])
    if number_occurrence == 1:
        with open("/Users/zhoujie/Desktop/pl_rest_subject_good_first_half_done.csv") as f:
            writer = csv.writer(f)
            writer.writerow(line)
