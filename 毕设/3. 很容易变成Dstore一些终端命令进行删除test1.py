import chardet
import os
def get_encoding(file):
	with open(file,'rb') as f:
		return chardet.detect(f.read())['encoding']

# file_name="C:\\Users\\Administrator\\Desktop\\stations.py"  #此处替换为你自己的文件路径
# encoding = get_encoding(file_name)
# print(encoding)

path = "/Users/zhoujie/Desktop/LREC2020-ENZH-SL/"
files = os.listdir(path)

for file in files:
	file_name = path + file
	encoding = get_encoding(file_name)
	print(file,encoding)

## 删除.DS_STORE隐藏文件
# 打开终端,并输入以下命令
# cd desktop
# find . -name '.DS_Store' -type f -delete

###用try else
# 删除用shell 删除DS_Store
# 然后再跑脚本程序

