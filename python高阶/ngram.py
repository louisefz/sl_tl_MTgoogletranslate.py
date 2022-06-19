import nltk
from nltk.corpus import gutenberg
import json
from operator import itemgetter
from collections import Counter

nltk.download("popular")

###文本处理成句子列表，以便在句子两边添加<s>与</s>

sentence_list1 = nltk.corpus.gutenberg.sents('austen-emma.txt') ###一个句子就是一个列表，句子列表中是分割好的token
print(sentence_list1[:10])
text1 = sentence_list1
#print(emma_wordlist)
###定义一个ngram的函数，从而形成3-gram和2-gram 根据公式p(3-gram)/p(2-gram),

def prob(sentence_list, n):
  ###对sentence_list进行lower()处理
  lower_sentence_list= []
  n_gram_list = []
  n_1gram_list = []
  for s in sentence_list:
    word_lower = [w.lower() for w in s]
    lower_sentence_list.append(word_lower)
  ###把大列表中的句子遍历，对每个小列表进行ngram处理
  for sent in lower_sentence_list:
    sentence_n = ["<s>"]*(n-1) + sent + ["</s>"]
    sentence_n_1 = ["<s>"]*(n-1) + sent + ["</s>"]
    n_gram_single = list(nltk.ngrams(sentence_n,n))
    n_1gram_single = list(nltk.ngrams(sentence_n_1,n-1))
    n_gram_list += n_gram_single ###这是所有n_gram合集list
    n_1gram_list += n_1gram_single ####这是n_1gram的合集list
####计算频率
  dictionary_n = dict(Counter(n_gram_list)) ####字典统计ngram的频率
  dictionary_n_1 = dict(Counter(n_1gram_list)) ####字典统计ngram的频率
  dictionary_prob = {}
  ndict_list = dictionary_n.keys()
  for key,value in dictionary_n.items():
    freq_ngram = value
    freq_n_1gram = dictionary_n_1[key[:-1]]
    probability = round(freq_ngram/freq_n_1gram,5)
    dictionary_prob[" ".join(key)] = probability
  return(dictionary_prob)
yidh = prob(text1,3)
print(yidh)

with open('/Users/zhoujie/Desktop/test/3gram_dict.json', 'w') as fp:
  json.dump(yidh, fp, sort_keys=True, indent=2)