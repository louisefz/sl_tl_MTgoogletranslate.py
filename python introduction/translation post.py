import requests
import json  ##有道翻译返回的结果是json，所以要用json进行解析
#### 一、查询单词
## 1.基于控制台获取的输入（输入就是待翻译词语）
content = "popular"             #input("请输入：")

## 2. 设定请求的url
url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
"""
##3. 简历post表单

post_form_word = {
    'i': content,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult':'dict',
    'client': 'fanyideskweb',
    'salt': '16398427136297',
    'sign': 'de1e5c43e4297de55d0c947d25c7ae34',
    'lts': '1639842713629',
    'bv': 'a9c06578fcaa460614d7467f0dcef37a',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}

## 4. 提交post请求
response_word = requests.post(url,data = post_form_word)

## 5. 接收响应结果，并解析提取
trans_json_word = response_word.text ###将json改成字符串的形式，用requests的text的属性
trans_dict_word = json.loads(trans_json_word) ##json的字符串转化成python的dict
##提取翻译的内容  去检查》》xhr》》preview》》拿到translateResult：tgt："djbajbv"
result_word = trans_dict_word["translateResult"][0][0]["tgt"]

## 6. 打印翻译结果
#print("词语查询结果：")
#print(result)
#print()
"""
#### 二、翻译段落
def translate(content):
    post_form_text = {
        'i': content,
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
    result_text_translation = "".join(result_text_list)
    print(result_text_translation)

var1 = translate("NHS staff are struggling with a “very, very depleted workforce”, the head of the Royal College of Nursing has warned, saying that staff want a course of action that allows them to care for patients safely. Pat Cullen told BBC Breakfast that nurses and other healthcare workers are “quite ill from the spin-off with Covid”. “[They] continue to be simply because their internal and personal resources are low going into this because of the number of hours that they’re working and the shifts they’ve been working on a very, very depleted workforce working in a fragile service leading up to this current wave,” she said.")





#### 三、翻译篇章

