###把嵌套元组转换成普通元组，然后相加
import webbrowser
dict1 = {"q": "gsgfs", "rtwt":"gbdgh", "a":"rtwdt", "gbadgh": "dga", "hethdgh": "dgsgsfbga"}
dict2 = {"hgb": "gdfdbfs", "afhdgn":"gbsdgnh", "134":"sfbdndt", "gbsgh": "afadhf", "asghethdgh": "wetdgsgsfbga"}
listx = []
for xx in dict1:
    yy = dict1[xx]
    tuplex = (xx,yy)
    listx.append(tuplex)
print(listx)
###变成没有内部括号的元组
dictx = dict(listx)
#print(type(dictx))
listw = []
for xxx in dictx:
    #print(dictx[xxx])
    listw.append(xxx)
    listw.append(dictx[xxx])
print(listw)
tupleq = tuple(listw)
print(tupleq)



GEN_HTML = "/Users/zhoujie/Desktop/data/test.html"
f = open(GEN_HTML,'w')
y = 0
list1 = []

for x in dict1.keys():
    y += 1
    list1.append(x)
    list1.append(dict1[x])
print(y)
tuple1 = tuple(list1)
tuple2 = ("remark",)
tuple3 = tuple2 + tuple1
print(tuple3)

list2=[]
p=0
for k in dict2:
    v = dict2[k]
    p += 1
    word_explain = k+" : "+v
    list2.append(word_explain)
    tuple4 = tuple(list2)
print(tuple4)
tuple3 = tuple3 +tuple4
print(p)



str1 = """<html>
<head></head>
<body>
<i><p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(192, 192, 192); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(192, 192, 192)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(192, 192, 192); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__11">%s</p></i>
<center><strong style = "font-size: 27px" data-darkmode-color-16402558296242="rgb(224, 40, 91)" data-darkmode-original-color-16402558296242="#fff|rgb(171, 25, 66)">EN-CH PAIR PARAGRAPHS</strong></center>
<center><strong data-darkmode-color-16402558296242="rgb(224, 40, 91)" data-darkmode-original-color-16402558296242="#fff|rgb(171, 25, 66)">%s</strong></center>
<center><strong data-darkmode-color-16402558296242="rgb(224, 40, 91)" data-darkmode-original-color-16402558296242="#fff|rgb(171, 25, 66)">%s</strong></center>
<p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__10"><br style="box-sizing: border-box; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)"></p>
<i><p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(192, 192, 192); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(192, 192, 192)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(192, 192, 192); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__11">本文原文来源于《卫报》，翻译部分调用有道翻译API仅供参开</p></i>

"""
para = """
<p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__11">%s</p>
<p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(192, 192, 192); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(192, 192, 192)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(192, 192, 192); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__11">%s</p>
<p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__10"><br style="box-sizing: border-box; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)"></p>
"""*(y-1)

str2 ="""
<p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__10"><br style="box-sizing: border-box; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)"></p>
<center><strong style = "font-size: 27px" data-darkmode-color-16402558296242="rgb(224, 40, 91)" data-darkmode-original-color-16402558296242="#fff|rgb(171, 25, 66)">VOCABULARY</strong></center>
"""

vocabulary  = """
<center><p>%s</p></center>
"""*p

str4 = """
</body>
</html>
"""
html1 = str1+para+str2+vocabulary+str4
print(html1)
article = html1 % tuple3

f.write(article)
f.close()

#webbrowser.open(GEN_HTML,new = 1)
