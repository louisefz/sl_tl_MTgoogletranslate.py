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




####创建一个分词器
tokenizer = ByteLevelBPETokenizer()
tokenizer.train(["/Users/zhoujie/Documents/AI/project/is_are/train_dataset/csvfile.txt"], vocab_size=50000,special_tokens=['<s>','<pad>','</s>','<unk>',',<mask>'])
tokenizer.save_model("/Users/zhoujie/Documents/AI/project/roberta/tokenizer")
#print(tokenizer.encode("the rabbit is jumping.").tokens)

tokenizer = ByteLevelBPETokenizer(
    "/Users/zhoujie/Documents/AI/project/roberta/tokenizer/vocab.json",
    "/Users/zhoujie/Documents/AI/project/roberta/tokenizer/merges.txt",
)
tokenizer._tokenizer.post_processor = BertProcessing(
    ("</s>", tokenizer.token_to_id("</s>")),
    ("<s>", tokenizer.token_to_id("<s>")),
)
#####有符号的tokenizer
tokenizer.enable_truncation(max_length=512)
print(tokenizer.encode("Mi estas Julien.").tokens)




# 定义模型的配置
config = RobertaConfig(
    vocab_size = 50000, # 词汇表大小
    max_position_embeddings = 514, # position的大小
    num_attention_heads = 12, # attention 头
    num_hidden_layers = 6, # 6层
    type_vocab_size = 1 # 指代 token_type_ids 的类别
)

# 创建 Roberta tokenizer
tokenizer = RobertaTokenizerFast.from_pretrained('/Users/zhoujie/Documents/AI/project/roberta/tokenizer', max_length=512)

# 初始化 model
roberta_model = RobertaForMaskedLM(config=config)
print(roberta_model.num_parameters())

dataset = LineByLineTextDataset(tokenizer=tokenizer, # 分词器
                                file_path='/Users/zhoujie/Documents/AI/project/is_are/train_dataset/csvfile.txt', # 文本数据
                                block_size=128) # 每批读取128行

data_collector = DataCollatorForLanguageModeling(tokenizer=tokenizer, # 分词器
                                                 mlm=True, # mlm模型
                                                 mlm_probability=0.15) # 15%的word进行mask
#print(data_collector)

trainArgs = TrainingArguments(
    output_dir='/Users/zhoujie/Documents/AI/project/roberta/tokenizer', # 输出路径
    overwrite_output_dir=True, # 可以覆盖之前的输出
    num_train_epochs=1, # 默认值
    per_gpu_train_batch_size=64,
    save_steps=10_000,
    save_total_limit=2,
    prediction_loss_only=True,
)

# ② trainer 定义

trainer = Trainer(
    model=roberta_model, # 模型对象
    args=trainArgs, # 训练参数
    data_collator=data_collector, # collector
    train_dataset=dataset # 数据集
)

trainer.train()
# 保存模型

trainer.save_model("/Users/zhoujie/Documents/AI/project/roberta/tokenizer")

predict_mask = pipeline('fill-mask',
                        model='/Users/zhoujie/Documents/AI/project/roberta/tokenizer',
                        tokenizer='/Users/zhoujie/Documents/AI/project/roberta/tokenizer')

print(predict_mask("oranges which contains much juice and vitamin C <mask> considered good."))


