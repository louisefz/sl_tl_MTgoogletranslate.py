import torch
from IPython.core.display import HTML
import numpy as np
from pytorch_transformers import BertTokenizer, BertForMaskedLM
import nltk
import collections


# previous version of `load_voacb`
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased')


###文件
with open('/Users/zhoujie/Documents/AI/project/is_are/master.csv', encoding='utf8') as f:
	text = f.read().splitlines()

for s in text:
    splits = s.split(',')
    #print(splits)
    item = "[CLS] " + splits[0] + " [SEP]"
    tokenized_text = tokenizer.tokenize(item)
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    ####segment
    segments_ids = [0] * len(tokenized_text)

    # Convert inputs to PyTorch tensors
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])

    # Load pre-trained model (weights)
    model = BertForMaskedLM.from_pretrained('bert-large-uncased')
    model.eval()
    masked_index = tokenized_text.index('[MASK]')
    # Predict all tokens
    with torch.no_grad():
        predictions = model(tokens_tensor, segments_tensors)

    predicted_index = torch.argmax(predictions[0][0][masked_index]).item()
    predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]
    print(predicted_token,s)


