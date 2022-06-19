import torch
from pytorch_transformers import BertForMaskedLM, BertTokenizer
import sys
import torch.nn.functional as F
import numpy
import csv

model = BertForMaskedLM.from_pretrained('bert-base-uncased') # replace large with base
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased') # replace large with base

csv_reader = csv.reader(open("/Users/zhoujie/Desktop/paper_project/sg_sva_mask_full_para_duplicate.csv"))
for line in csv_reader:
	print(line)
	print(line[4])
	item = "[CLS] " + line[4].replace("\n","") + " [SEP]"
	print(item)
	tokenized_text = tokenizer.tokenize(item)
	words = line[4].replace("\n","").split(' ')  ###将句子变成token的形式
	print(words)
	masked_index = words.index('[MASK]') + 1  ###找到[mask]在句子中是第几位
	indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
	tens = torch.LongTensor(indexed_tokens).unsqueeze(0)
	output = model(tens)
	res = output[0]
	res = res[0, masked_index]
	# Softmax
	res = torch.nn.functional.softmax(res, -1)  ###dim=-1
	# print(res)
	word_ids = tokenizer.convert_tokens_to_ids([line[1], line[2]])
	# print(word_ids)
	scores = res[word_ids]
	# print(type(scores))
	list = scores.detach().numpy().tolist()
	print(list)
	print(type(list[0]))
	if list[0] > list[1]:
		line.append(line[1])
	elif list[0] < list[1]:
		line.append(line[2])
	else:
		line.append(line[1]+" / "+ line[2])
	with open("/Users/zhoujie/Desktop/paper_project/sg_sva_mask_full_para_duplicate_bert_base.csv", "a+") as f:
		writer = csv.writer(f)
		writer.writerow(line)

