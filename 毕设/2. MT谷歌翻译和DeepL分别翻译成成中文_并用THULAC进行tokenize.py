# 一句一句翻译

import re
import html
from urllib import parse
import requests
import os
import thulac
import deepl

GOOGLE_TRANSLATE_URL = 'http://translate.google.com/m?q=%s&tl=%s&sl=%s'

def Google_translate(text, to_language="auto", text_language="auto"):

    text = parse.quote(text)
    url = GOOGLE_TRANSLATE_URL % (text,to_language,text_language)
    response = requests.get(url)
    data = response.text
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    result = re.findall(expr, data)
    if (len(result) == 0):
        return ""

    return html.unescape(result[0])

def deepl_translate(sent):
    translator = deepl.Translator("7adebb8d-2ff7-5a2e-0fa5-b626408c1606:fx")
    result = translator.translate_text(sent, target_lang="ZH")
    return result

print(Google_translate("我喜欢你。", "en","zh-CN")) #汉语转英语
print(Google_translate("你吃饭了么？", "ja","zh-CN")) #汉语转日语
print(Google_translate("about your situation", "zh-CN","en")) #英语转汉语
path = "/Users/zhoujie/Desktop/LREC2020-ENZH-SL"
files = os.listdir(path)

thu1 = thulac.thulac(seg_only=True)
import time
time.clock = time.time


i = 1
#
list_input = []
for file in files:
    with open("/Users/zhoujie/Desktop/LREC2020-ENZH-SL/"+ file) as f:
        text_list = f.read().split("\n")
        for s in text_list:
            translation_g = Google_translate(s,"zh-CN","en")
            translation_d = str(deepl_translate(s))
            # print(translation_g)
            # print(translation_d)
            token_trans_g = "".join(thu1.cut(translation_g, text = True))
            token_trans_d = "".join(thu1.cut(translation_d, text=True))

            sentence = str(i) + "\n" + s + "\n" + token_trans_g + "\n" + token_trans_d + "\n"
            print(sentence)
            i += 1
            list_input.append(sentence)
            input_s = "".join(list_input)
        list_input.clear()
        i = 1
        with open("/Users/zhoujie/Desktop/LREC2020-ENZH-translation/" + file,"w") as o:
            o.write(input_s)








