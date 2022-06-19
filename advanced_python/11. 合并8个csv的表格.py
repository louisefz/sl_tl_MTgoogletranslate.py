import os, glob
import pandas as pd

# ###合并8张csv表格
# path = "/Users/zhoujie/Desktop/test_merge"
# all_files = glob.glob(os.path.join(path, "*.csv"))
#
# df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
# df_merged = pd.concat(df_from_each_file, ignore_index=True)
# df_merged.to_csv("/Users/zhoujie/Desktop/test_merge/merged.csv")

# ####找到平均值NER, Adj, Adv
df = pd.read_csv('/Users/zhoujie/Desktop/test_merge/merged.csv')
df['Adj%'] = df['Adj'] /df['number_token']
df['Adv%'] = df['Adv'] /df['number_token']
df['NER%'] = df['NER'] /df['number_token']
print(df)
df.to_csv("/Users/zhoujie/Desktop/test_merge/merged.csv")


