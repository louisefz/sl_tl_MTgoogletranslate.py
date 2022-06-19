import torch
from pytorch_transformers import BertForMaskedLM, BertTokenizer
import sys
import torch.nn.functional as F
import numpy as np

from pathlib import Path
from tokenizers import ByteLevelBPETokenizer, BertWordPieceTokenizer
from tokenizers.processors import BertProcessing
import os
import json
import torch
import torch.nn as nn
import torch.optim as optim
import torch

from transformers import RobertaConfig, RobertaTokenizer, RobertaModel, RobertaForMaskedLM, RobertaTokenizerFast, PreTrainedTokenizerFast
from transformers import LineByLineTextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments, pipeline



model = BertForMaskedLM.from_pretrained('bert-large-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased')


s = "the question of whether we should demand a payment for our services [MASK] not even discussed."



#print(splits[0]) ####句子，因为cvs有4列，知识读取[0]第一列
item = "[CLS] " + s + " [SEP]" #首尾都加上符号
tokenized_text = tokenizer.tokenize(item)
#print(tokenized_text)

# Find index of the masked token 找到所有[mask]的index
words = s.split(' ') ###将句子变成token的形式
masked_index = words.index('[MASK]') + 1  ###找到[mask]在句子中是第几位
#print(masked_index)

# Convert target tokens to vocabulary indices,将文本中的所有token转化成index
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
#print(indexed_tokens)

# Convert inputs to Pytorch tensors
tens = torch.LongTensor(indexed_tokens).unsqueeze(0) ####一句话，这个tensor只有一行，因此作softmax之后，tensor的softmax值相加为1， dim=-1表示，每一行的tensor值相加为1
#print(tens)

# If you have a GPU, put everything on cuda
#tens = tens.to('cuda')

# Determine resulting activation of masked position
output = model(tens)
#print(output)
res = output[0]
#print(res)

# Determine resulting activation of masked position
res = res[0,masked_index]
#print(res)   #####mask的tensor参数

# Softmax
res = torch.nn.functional.softmax(res, -1) ###dim=-1
print(res)
word_ids = tokenizer.convert_tokens_to_ids(['is', 'are'])
print(word_ids)
scores = res[word_ids]
print(scores)
list = scores.detach().numpy().tolist()
print(list)
print(type(list[0]))
if list[0] >list[1]:
	print("is", s)
else:
	print("are", s)