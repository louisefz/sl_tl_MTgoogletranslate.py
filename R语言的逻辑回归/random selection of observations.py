import pandas as pd
import os

#####随机抽样csv文件，生成新的csv文件
#data = pd.read_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_academy_announce.csv')
#sample = data.sample(frac=0.115, random_state=5, axis=0)
#sample.to_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_academy_announce1.csv',encoding='utf_8_sig')

#data = pd.read_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_academy_declare.csv')
#sample = data.sample(frac=0.116, random_state=5, axis=0)
#sample.to_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_academy_declare1.csv',encoding='utf_8_sig')


#data = pd.read_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_fiction_announce.csv')
#sample = data.sample(frac=0.10, random_state=5, axis=0)
#sample.to_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_fiction_announce1.csv',encoding='utf_8_sig')


#data = pd.read_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_fiction_declare.csv')
#sample = data.sample(frac=0.099, random_state=5, axis=0)
#sample.to_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_fiction_declare1.csv',encoding='utf_8_sig')


#data = pd.read_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_news_announce.csv')
#sample = data.sample(frac=0.052, random_state=5, axis=0)
#sample.to_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_news_announce1.csv',encoding='utf_8_sig')


#data = pd.read_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_news_declare.csv')
#sample = data.sample(frac=0.053, random_state=5, axis=0)
#sample.to_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_news_declare1.csv',encoding='utf_8_sig')


#data = pd.read_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_spoken_announce.csv')
#sample = data.sample(frac=0.454, random_state=5, axis=0)
#sample.to_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_spoken_announce1.csv',encoding='utf_8_sig')


#data = pd.read_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_spoken_declare.csv')
#sample = data.sample(frac=0.446, random_state=5, axis=0)
#sample.to_csv('/Users/zhoujie/Documents/corpus/项目/csv/project_spoken_declare1.csv',encoding='utf_8_sig')



######将随机生成的csv文件合并生成一个新的csv文件
Folder_Path = "/Users/zhoujie/Documents/corpus/project/csv/sample_csv"          #要拼接的文件夹及其完整路径，注意不要包含中文
SaveFile_Path = "/Users/zhoujie/Documents/corpus/project/csv/big_csv"      #拼接后要保存的文件路径
SaveFile_Name = "/Users/zhoujie/Documents/corpus/project/csv/big_csv_form.csv"               #合并后要保存的文件名


os.chdir(Folder_Path)
file_list = os.listdir()
df = pd.read_csv(Folder_Path +'\\'+ file_list[0])
df.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False)
for i in range(1,len(file_list)):
    df = pd.read_csv(Folder_Path + '\\'+ file_list[i])
    df.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False, header=False, mode='a+')

