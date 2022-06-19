import os

path = "/Users/zhoujie/Desktop/LREC2020-ENZH-annotatedCorpus/"
list_file = []
list_sl = []
files = os.listdir(path)
for file in files:
    if os.path.splitext(file)[1] == ".crp":
        list_file.append(file)
print(list_file)

for lf in list_file:
    with open("/Users/zhoujie/Desktop/LREC2020-ENZH-annotatedCorpus/" + lf, "r") as f:
        x = f.read()
        print(x)
        list_text = x.split("\n")

        # print(list_text)
        for index, ele in enumerate(list_text):
            if index%3 == 2:
                list_sl.append(ele)
        text = "\n".join(list_sl)
        list_sl.clear()
        with open("/Users/zhoujie/Desktop/HT_ZH/"+lf, "w") as p:
            p.write(text)

