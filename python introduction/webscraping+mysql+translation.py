import bs4
import requests
import spacy  # lemmatize
import time
import pandas
import pymysql ###to connect mysql
import numpy # conform the structure of mysql(use tuple)
import re
import json #webscraping for translation
import webbrowser

##get the date of today 因为每天有2篇文章，所以需要两个日期，做成一个Date表格，最后让日期好存在mysql中
t = time.localtime()
Date = []
date1 = str(t.tm_year) + "-" + str(t.tm_mon)+ "-" + str(t.tm_mday)
Date.append(date1)
date2 = str(t.tm_year) + "-" + str(t.tm_mon)+ "-" + str(t.tm_mday)
Date.append(date2)
print(Date)



### webscraping, find the guarian's some information
r_guardian_homepage = requests.get('https://www.theguardian.com/international')
html = r_guardian_homepage.text
#print(html)

html_guardian_homepage = r_guardian_homepage.text

soup_guardian_homepage = bs4.BeautifulSoup(html_guardian_homepage, "lxml") 
#print(soup_guardian_homepage)

#title = soup_guardian_homepage.select("body > div.facial-page> div.l-side-margins > div.facial-page > section >  ")

Cover_picture = []
# 需要的封面图：上传至微信公众号的封面
Cover_picture = []
news1_image = soup_guardian_homepage.select("img")
for image in news1_image[:1]:
    img1 = image["src"]
    Cover_picture.append(img1)
for image in news1_image[1:2]:
    img2 = image["src"]
    Cover_picture.append(img2)
    #print(Cover_picture)
URL = []
Title = []
# 标题和URL的提取
news1_title = soup_guardian_homepage.select("h3")
for title in news1_title[:1]:
    url1 = title.a["href"]
    TITLE1 = title.text.strip(" ")
    Title.append(TITLE1)
    URL.append(url1)
for title in news1_title[1:2]:
    url2 = title.a["href"]
    TITLE2 = title.text.strip(" ")
    Title.append(TITLE2)
    URL.append(url2)
    #print(Title,URL)
#print(Cover_picture)
#print(URL)
# 建立爬取首页的文件，设计一个数据库
tuple_list1 = []
for A,B,C,D in zip(Date, Title, URL, Cover_picture):
    tuple2 = (A,B,C,D)
    #print(tuple2)
    tuple_list1.append(tuple2)
#print(tuple_list1)




###store informtion into MySql
connection3 = pymysql.connect(host = "localhost",
                             port = 3306,
                             user = "root",
                             password = "Dchopj0896,/0110",
                             database= "guardian",
                             charset= "utf8mb4") ### MySQL的“utf8mb4”是真正的“UTF-8”   MySQL的“utf8”是一种“专属的编码”，它能够编码的Unicode字符并不多。

cursor3 = connection3.cursor()


sql1 = "insert into t1(Date, Title, URL, Cover_picture) values(%s, %s, %s, %s);"
cursor3.executemany(sql1, tuple_list1)
connection3.commit()





# take the url of the detail pages from MySql, and then open it for webscraping调取数据库中的URL，然后打开，继续爬虫
# 读取两个网站的数据
Title = []
Top_picture = Cover_picture
Remark1 = []
Paragraph = []
####找到对应的链接URL：

cursor3.execute("select URL from t1 where TO_DAYS(Date) =  TO_DAYS(NOW());")
URL_mysql = cursor3.fetchall()
#print(URL_mysql)
###将元组转化成列表 turn the scraped data into tuple so that it can be easily stored into MySql
list_URL = list(URL_mysql)
URL_MYSQL_LIST = []
for tuple in list_URL:
    list_tuple = list(tuple)
    #print(list_tuple)
    for x in list_tuple:
        #print(x)
        URL_MYSQL_LIST.append(x)
#print(URL_MYSQL_LIST)
for link in URL_MYSQL_LIST:
    request_guardian_detail = requests.get(link)
    html_guardian_detail = request_guardian_detail.text
    soup_guardian_detail = bs4.BeautifulSoup(html_guardian_detail, "lxml")
#print(link,soup_guardian_detail)
#找到标题 find titles of news
#if soup_guardian_detail.find("div",{"data_component":"youtube_atom"}): 先判断是不是live的结构，如果是则用这种结构进行查看相关的内容
    if soup_guardian_detail.find_all("a",{"class":"timeline__link"}):
        Title1 = soup_guardian_detail.find("h1").text
        #print(Title1)
        Remark = soup_guardian_detail.find("figcaption",{"class":"caption caption--main caption--img"}).text.strip()
        #print(Remark)
        Paragraph1 = soup_guardian_detail.find("div", {"class":"block-elements block-elements--no-byline"}).text
        #print(Paragraph1)
        Title.append(Title1)
        Remark1.append(Remark)
        Paragraph.append(Paragraph1+"\n")

    else: ###如果是普通的结构，就用下面的代码
        Title1 = soup_guardian_detail.find("h1").text
        #print(Title1)
        Title.append(Title1)
        Top_picture_list = soup_guardian_detail.find_all("div", {"data-gu-name": "media"})
        for picture1 in Top_picture_list:
            Top_picture1 = picture1.find("img")
            #Top_picture的注释：（包括图片注释和作者）
            Remark = picture1.find("figcaption").text.strip()
            #print(Remark)
            Remark1.append(Remark)
        #正文部分paragraph ###paragraphs in the detail pages
            Para = []
            body_list= soup_guardian_detail.find_all("p",{"class":"dcr-o5gy41"})
            for p in body_list:
                Paragraph2 = p.text
                Para.append(Paragraph2)
            print(Para)
            Paragraph1 = "\n".join(Para)
            #print(Paragraph1)
            Paragraph.append(Paragraph1)



#print(Title)
#print(Top_picture)
#print(Remark1)
#print(Paragraph)

#print(Top_picture)

tuple_list = []
for a,b,c,d,e in zip(Date, Title, Top_picture, Remark1, Paragraph):
    tuple1 =(a,b,c,d,e)
    #print(tuple1)
    tuple_list.append(tuple1)
#print(tuple_list)



###store the information of the detail pages into MySql as t2
connection3 = pymysql.connect(host = "localhost",
                             port = 3306,
                             user = "root",
                             password = "Dchopj0896,/0110",
                             database= "guardian",
                             charset= "utf8mb4")

cursor4 = connection3.cursor()
sql = "insert into t2(Date, Title, Top_picture, Remark1, Paragraph) values(%s, %s, %s, %s, %s);"
cursor4.executemany(sql,tuple_list)
connection3.commit()







####翻译任务从t2中选取
sql_text1 = "select Title, Paragraph from t2 where TO_DAYS(Date) =  TO_DAYS(NOW()) and ID%2 = 1;"
cursor4.execute(sql_text1)
re_text1 = cursor4. fetchall()
#print(re_text)
re_text_list1 = list(re_text1)
textlist1_nested = []
for y1 in re_text_list1:
    y1_list = list(y1)
    #print(y1_list)
    for z1 in y1_list:
        #print(z1)
        textlist1_nested.append(z1)
Text1_list = textlist1_nested
Text1_str = "\n".join(Text1_list)
#print(Text1_str)

#### from t2, texts are retrieved and then translated into Chinese by calling youdao.com's API
sql_text1 = "select Title, Paragraph from t2 where TO_DAYS(Date) =  TO_DAYS(NOW()) and ID%2 = 0;"
cursor4.execute(sql_text1)
re_text2 = cursor4. fetchall()
#print(re_text)
re_text_list2 = list(re_text2)
textlist2_nested = []
for y2 in re_text_list2:
    y2_list = list(y2)
    #print(y1_list)
    for z2 in y2_list:
        #print(z2)
        textlist2_nested.append(z2)
Text2_list = textlist2_nested
Text2_str = "\n".join(Text2_list)
#print(Text2_str)

###### as to insert translation for every paragraph in text1 and text2, I will segment paragraphs from each other referring to "\n"
Text1_newlinelist = Text1_str.split("\n")
Text2_newlinelist = Text2_str.split("\n")
for element1 in Text1_newlinelist:
    if "" in Text1_newlinelist:
        Text1_newlinelist.remove("")
for element2 in Text2_newlinelist:
    if "" in Text2_newlinelist:
        Text2_newlinelist.remove("")

print(Text1_newlinelist)
print(Text2_newlinelist)

#### turn tokens into lemma, and find if there are GRE words in the texts;
# the text is segmented into a list of paragraphs
# 处理第一篇文章，（1）将其处理成lemma，找到gre的词汇 （2）将其处理成\n 方便调API，一段一段的翻译
####1）将其处理成lemma，找到gre的词汇
Text_lemma1 = []
Text_lemma2 = []
nlp = spacy.load("en_core_web_sm")
text1_lemma = nlp(Text1_str)
text2_lemma = nlp(Text2_str)
for el in text1_lemma:
    lemma_text1 = el.lemma_
    if lemma_text1 not in Text_lemma1:
        Text_lemma1.append(lemma_text1)
#print(Text_lemma1)
for el in text2_lemma:
    lemma_text2 = el.lemma_
    if lemma_text2 not in Text_lemma2:
        Text_lemma2.append(lemma_text2)
#print(Text_lemma2)


# webscraping for GRE words website, and create t3 to store GRE words.
# 将docx做成docx_list,与t3_list(GRE词汇表)进行遍历匹配，找到文章中出现的GRE词汇，进行翻译
# 爬虫GRE词汇，并存在mysql的t3中
request_gre = requests.get("https://www.vocabulary.com/lists/128536")
html_gre = request_gre.text
soup_gre = bs4.BeautifulSoup(html_gre, "lxml")
vocabulary_list = soup_gre.find_all("a",{"class":"word dynamictext"})
Vocabulary = []
for vocabulary in vocabulary_list:
    word = vocabulary.text
    Vocabulary.append(word)




connection3 = pymysql.connect(host = "localhost",
                             port = 3306,
                             user = "root",
                             password = "Dchopj0896,/0110",
                             database= "guardian",
                             charset= "utf8mb4")


cursor3 = connection3.cursor()
sql = "insert into t3 (Vocabulary) values('%s');"
for Vocabulary in Vocabulary:
    Vocabulary = re.sub('\s', '', Vocabulary)
    cursor3.execute(sql % (Vocabulary))
connection3.commit()



connection3 = pymysql.connect(host = "localhost",
                             port = 3306,
                             user = "root",
                             password = "Dchopj0896,/0110",
                             database= "guardian",
                             charset= "utf8mb4")

cursor3 = connection3.cursor()
cursor3.execute("select Vocabulary from t3;")
result_GRE = cursor3.fetchall()
#print(result)
df_gre = pandas.DataFrame(result_GRE)

### GRE words serve as referece, and they are turned into a list so that the GRE words can be looped.
# 读取t3中的GRE词汇，并转化成列表的形式进行遍历
GRE_mysql_list = numpy.array(df_gre).tolist()
#print(GRE_mysql_list)
GRE_list=[]
for word in GRE_mysql_list:
    GRE_word = "".join(word)
    GRE_list.append(GRE_word)
#print(GRE_list)

######match lemmas of texts with GRE word list
# text1与text2中的GRE词汇
#### 1. 匹配文章1中的与gre中的词
text1_word_translation1 = []
for x1 in Text_lemma1:
    if x1 in GRE_list:
        #print("1：", x1)
        text1_word_translation1.append(x1)

#### 2. 匹配文章2中的与gre中的词
text2_word_translation2 = []
for x2 in Text_lemma2:
    if x2 in GRE_list:
        #print("2：", x2)
        text2_word_translation2.append(x2)
print(text2_word_translation2)


#### translate GRE words in the texts into Chinese
# 一、查询单词
## 1.基于控制台获取的输入（输入就是待翻译词语）
def store_into_mysql(text_word_translation):
    #dict1_w_trans = {}
    list1_w_trans = []
    for ww in text_word_translation:
        #print(type(ww))
        content1 = ww
        url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        post_form_text = {
            'i': content1,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult':'dict',
            'client': 'fanyideskweb',
            'salt': '16398460630419',
            'sign': '04c53da7aecf41b9aff38698d847e1f5',
            'lts': '1639846063041',
            'bv': 'a9c06578fcaa460614d7467f0dcef37a',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        response_text = requests.post(url,data = post_form_text)
        trans_json_text = response_text.text ###将json改成字符串的形式，用requests的text的属性
        trans_dict_text = json.loads(trans_json_text) ##json的字符串转化成python的dict
        ##提取翻译的内容  去检查》》xhr》》preview》》拿到translateResult：tgt："djbajbv"
        result_list = trans_dict_text["translateResult"][0]
        result_text_list = []
        for dict_tgt in result_list:
            result_text = dict_tgt["tgt"]
            result_text_list.append(result_text)
        result_word1_translation = "".join(result_text_list)
        #print(result_word1_translation)
        tuple_w = (ww, result_word1_translation)
        list1_w_trans.append(tuple_w)
    print(list1_w_trans)
    ####将翻译的内容分别储存到mysql的guardian数据库的t5,t6,t7,t8表格中

    connection3 = pymysql.connect(host = "localhost",
                                 port = 3306,
                                 user = "root",
                                 password = "Dchopj0896,/0110",
                                 database= "guardian",
                                 charset= "utf8mb4")

    cursor4 = connection3.cursor()
    if text_word_translation == text1_word_translation1:
        sql_w1 = "insert into w1 (Date, w1, Trans) values(NOW(), %s, %s);"
        cursor4.executemany(sql_w1, list1_w_trans)
        connection3.commit()
    elif text_word_translation == text2_word_translation2:
        sql_w2 = "insert into w2 (Date, w2, Trans) values(NOW(), %s, %s);"
        cursor4.executemany(sql_w2, list1_w_trans)
        connection3.commit()
    elif text_word_translation == Text1_newlinelist:
        sql_text1 = "insert into text1 (Date, text1, Trans) values(NOW(), %s, %s);"
        cursor4.executemany(sql_text1, list1_w_trans)
        connection3.commit()
    elif text_word_translation == Text2_newlinelist:
        sql_text2 = "insert into text2 (Date, text2, Trans) values(NOW(), %s, %s);"
        cursor4.executemany(sql_text2, list1_w_trans)
        connection3.commit()

store_into_mysql(text1_word_translation1)
store_into_mysql(text2_word_translation2)
store_into_mysql(Text1_newlinelist)
store_into_mysql(Text2_newlinelist)



####   将htlm导入到微信公众号的后台中















# 调微信的api,上传docx，然后发送

# 做一个cron job，每天早上运行程序，每天生成一个docx













