
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models
import pandas as pd
import numpy as np
import os
import jieba
import xlwt as xw
from xlutils.copy import copy
import xlrd as xr
'''
df = pd.read_excel('/Users/zhoujie/Documents/corpus/project/csv/big_csv/project_sentiment.xlsx',usecols=[3], names = None)
df_list = df.values.tolist()
result = []
for x in df_list:
    if x[0] != "sentence":
        result.append(x[0])
print(result)

senti_list_large = []
for x in result:
    text = x
'''
try:
    cred = credential.Credential("AKID2tVrwkHZaqse9NK1RaS4PTGm21jCQM1P", "81e04tRhhQs3yd18yXqsc5IEtGMDnb8P")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "nlp.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

    req = models.SentimentAnalysisRequest()
    params = {
        "Text": "this hypothetical legislative decision has not been announced in advance, so the ideal of protected expectations has in that way been compromised.",
        "Mode": "3class"
    }
    req.from_json_string(json.dumps(params))

    resp = client.SentimentAnalysis(req)
    str1 = resp.to_json_string()
    str2 = str1.strip("{").strip("}")
    print(str2)
    list1 = str2.split(",")
    senti_str = list1[3]
    senti_list = senti_str.split(":")
    senti = senti_list[1].strip(""" " """)
    #print(senti)
    #senti_list_large.append(senti)


except TencentCloudSDKException as err:
    print(err)
"""
print(senti_list_large)


file = '/Users/zhoujie/Documents/corpus/project/csv/big_csv/project_sentiment.xlsx'
style = xw.easyxf()
oldwb = xr.open_workbook(file)
newwb = copy(oldwb)
newws = newwb.get_sheet(0)
for i in range(len(senti_list_large)):
    newws.write(i, 0, senti_list_large[i],style) #把列表a中的元素逐个写入第一列，0表示实际第1列,i+1表示实际第i+2行
newwb.save(file)#保存修改
"""



