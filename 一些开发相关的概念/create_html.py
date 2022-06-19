import bs4
import requests
import spacy
import time
import pandas
import pymysql
import numpy
import re
import json
import webbrowser
import os
####   将本地mysql的数据库写进html
###选取需要的数据


connection3 = pymysql.connect(host = "localhost",
                             port = 3306,
                             user = "root",
                             password = "Dchopj0896,/0110",
                             database= "guardian",
                             charset= "utf8mb4")
###选Remark
cursor3 = connection3.cursor()
cursor3.execute("select Remark1 from t2 where ID%2=1 and TO_DAYS(Date) =  TO_DAYS(NOW());")
result_Remark1 = cursor3.fetchall()
cursor3.execute("select Remark1 from t2 where ID%2=0 and TO_DAYS(Date) =  TO_DAYS(NOW());")
result_Remark2 = cursor3.fetchall()
print(result_Remark1)
#print(result_Remark2)
list_result_Remark1 = list(result_Remark1)
for x in list_result_Remark1:
    tuple_remark1 = x
    #print(type(tuple_remark1))

###选title+选中英对照的段落paragraph

cursor3 = connection3.cursor()
cursor3.execute("select text1, Trans from text1 where ID%2=1 and TO_DAYS(Date) =  TO_DAYS(NOW());")
result_text1 = cursor3.fetchall()
cursor3.execute("select text2, Trans from text2 where ID%2=0 and TO_DAYS(Date) =  TO_DAYS(NOW());")
result_text2 = cursor3.fetchall()
#print(result_text1)
#print(result_text2)

###选中英对照的段落gre words
cursor3 = connection3.cursor()
cursor3.execute("select w1, Trans from w1 where ID%2=1 and TO_DAYS(Date) =  TO_DAYS(NOW());")
result_w1 = cursor3.fetchall()
cursor3.execute("select w2, Trans from w2 where ID%2=0 and TO_DAYS(Date) =  TO_DAYS(NOW());")
result_w2 = cursor3.fetchall()
#print(result_w1)
#print(result_w2)
tuple_nest1_list = list(result_w1)
#print(tuple_nest1_list)
list_result_w1 = []
for tuple11 in tuple_nest1_list:
    nest_list_result_w1 = list(tuple11)
    #print(nest_list_result_w1)
    str_result_w1 = " : ".join(nest_list_result_w1)
    #print(str_result_w1)
    list_result_w1.append(str_result_w1)

number_w1 = len(list_result_w1)
tuple_w1 = tuple(list_result_w1)




tuple_nest1 = result_text1
tuple_nest2 = result_text2
#print(tuple_nest1)
#print(tuple_nest2)

####   将嵌套tuple_nest变成普通元组tuple_large
tuple_nest1_list = list(tuple_nest1)
#print(tuple_nest1_list)
list_large = []
for tuple11 in tuple_nest1_list:
    nest_list = list(tuple11)
    print(nest_list)

    for xx in nest_list:
        #print(xx)
        list_large.append(xx)
number_body = len(tuple_nest1_list)
tuple_large = tuple_remark1 + tuple(list_large) + tuple_w1
#print(tuple_large)

text1_name = "_text1"
t = time.localtime()
date_today = str(t.tm_year) + "_" + str(t.tm_mon)+ "_" + str(t.tm_mday)
#print(date_today)
path_text1 = "/Users/zhoujie/Desktop/data/" + date_today + text1_name + ".html"
f = open(path_text1,'w')




str1 = """<html>
<head></head>
<body>
<i><p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(192, 192, 192); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(192, 192, 192)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(192, 192, 192); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__11">%s</p></i>
<center><strong style = "font-size: 23px" data-darkmode-color-16402558296242="rgb(224, 40, 91)" data-darkmode-original-color-16402558296242="#fff|rgb(171, 25, 66)">EN-CH PAIR PARAGRAPHS</strong></center>
<center><strong data-darkmode-color-16402558296242="rgb(224, 40, 91)" data-darkmode-original-color-16402558296242="#fff|rgb(171, 25, 66)">%s</strong></center>
<center><strong data-darkmode-color-16402558296242="rgb(224, 40, 91)" data-darkmode-original-color-16402558296242="#fff|rgb(171, 25, 66)">%s</strong></center>
<p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__10"><br style="box-sizing: border-box; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)"></p>
<i><p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(192, 192, 192); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(192, 192, 192)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(192, 192, 192); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__11">本文原文来源于《卫报》，翻译部分调用有道翻译API仅供参考</p></i>
"""

para = """
<p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__11">%s</p>
<p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(192, 192, 192); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(192, 192, 192)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(192, 192, 192); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__11">%s</p>
<p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__10"><br style="box-sizing: border-box; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)"></p>
"""* (number_body-1)

str2 ="""
<p style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)" data-style="box-sizing: border-box; line-height: 1.9; font-size: 15px; color: rgb(51, 51, 51); padding-right: 8px; padding-left: 8px; overflow: hidden;" class="js_darkmode__10"><br style="box-sizing: border-box; visibility: visible;" data-darkmode-color-16402124319927="rgb(163, 163, 163)" data-darkmode-original-color-16402124319927="#fff|rgb(51, 51, 51)"></p>
<center><strong style = "font-size: 23px" data-darkmode-color-16402558296242="rgb(224, 40, 91)" data-darkmode-original-color-16402558296242="#fff|rgb(171, 25, 66)">VOCABULARY</strong></center>
"""

vocabulary  = """
<p>%s</p>
"""*number_w1

str4 = """
</body>
</html>
"""

html1 = str1+para+str2+vocabulary+str4
print(html1)
article = html1 % tuple_large

f.write(article)
f.close()

