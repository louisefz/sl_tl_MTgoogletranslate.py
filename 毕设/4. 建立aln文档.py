import os
import re
files = os.listdir("/Users/zhoujie/Desktop/LREC2020-ENZH-translation")
print(files)
index_list = []

for file in files:

    with open("/Users/zhoujie/Desktop/LREC2020-ENZH-translation/" + file) as f:
        text = f.read()
        text_list = text.split("\n")
        for i, s in enumerate(text_list):
            if i%3 == 0:
                index_list.append(text_list[i])
        input_text = "\n".join(index_list)
        with open("/Users/zhoujie/Desktop/LREC2020-ENZH-translation/" + re.sub(".crp",".aln",file),"w") as o:
            o.write(input_text)


