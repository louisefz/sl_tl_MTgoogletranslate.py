import os
import pandas as pd
def token(path):
    number_token_list = []
    mean_len_token_list = []
    total_len = 0
    with open(path) as f:
        text_list = f.read().split("\n")
        for s in text_list:
            w_list = s.split(" ")
            number_token = len(w_list)
            number_token_list.append(number_token)

            for w in w_list:
                print(w)
                total_len += len(w)
            # mean_len_token = total_len / number_token
            mean_len_token = format(total_len/number_token,".4f")
            mean_len_token_list.append(mean_len_token)
            total_len = 0
        return number_token_list, mean_len_token_list

print(token("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json_test/txt/CONVRSN_all_26_clean.txt"))

g = os.walk("/Users/zhoujie/Desktop/logistic_reg_project/all_big_data/clean_data_json_test/txt")
for path,dir_list,file_list in g:
    for file in file_list:
        file_path = os.path.join(path, file)
        new_path = file_path.replace("txt", "csv")
        number_token_list, mean_len_token_list = token(file_path)
        df1 = pd.read_csv(new_path)
        df1["number_token"] = number_token_list
        df1.to_csv(new_path, index=False, sep=',')
        df1 = pd.read_csv(new_path)
        df1["mean_len_token"] = mean_len_token_list
        df1.to_csv(new_path, index=False, sep=',')


