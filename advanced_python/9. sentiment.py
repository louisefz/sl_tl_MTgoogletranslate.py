import requests
import os
import pandas as pd
import json
def sentiment(sentence):
    url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

    querystring = {"text":sentence}

    headers = {
        "X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com",
        "X-RapidAPI-Key": "893b58a3bemshd694cf2f45a17d9p1df68ajsn520f2dc5c028"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    dict_result = json.loads(response.text)
    return dict_result

g = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json_test/txt")
sent_type_list = []
sent_score_list = []
for path,dir_list,file_list in g:
    for file in file_list:
        file_path = os.path.join(path, file)
        new_path = file_path.replace("txt", "csv")
        with open(file_path) as f:
            s_list = f.read().split("\n")
        print(file_path)
        for s in s_list:
            sent_result = sentiment(s)
            sent_type = sent_result["type"]
            sent_type_list.append(sent_type)
            sent_score = format(sent_result["score"],"4f")
            sent_score_list.append(sent_score)
        print(sent_type_list)
        df1 = pd.read_csv(new_path)
        df1["sent_type"] = sent_type_list
        df1.to_csv(new_path, index=False, sep=',')
        df1 = pd.read_csv(new_path)
        df1["sent_score"] = sent_score_list
        df1.to_csv(new_path, index=False, sep=',')
        sent_type_list.clear()
        sent_score_list.clear()


