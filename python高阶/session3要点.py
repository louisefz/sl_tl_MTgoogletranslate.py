
##NER的用法
doc = "adjbjabv"
doc.ents
for x in doc.ents:
    print(x.text)
    print(x.label)

####NER可视化
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_md')
doc = nlp(u"Local health officials in the Iraqi Shia city of Najaf said \
an Iranian theology student was the first positive case of the virus, Reuters reports.")
spacy.displacy.render(doc, jupyter=True, style='ent')

# Python 字符串前面加u,r,b,f的含义
# 字符串前加u，后面字符串以 Unicode格式进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。
# 例如exp = u"我是含有中文字符组成的字符串。"

#字符串前加r：去掉反斜杠的转移机制。（特殊字符：即那些，反斜杠加上对应字母，表示对应的特殊含义的，比如最常见的”\n”表示换行，”\t”表示Tab等。 ）
# 应用：
# 常用于正则表达式，对应着re模块。




####dependency可视化
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a sentence.")
displacy.render(doc, style="dep", jupyter=True, options={'compact':True, 'font':'Arial'})