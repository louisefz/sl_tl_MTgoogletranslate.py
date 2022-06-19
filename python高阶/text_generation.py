from ngram import prob
from predict import predict_next_word
import random
import nltk
sentence_list1 = nltk.corpus.gutenberg.sents('austen-emma.txt') ###一个句子就是一个列表，句子列表中是分割好的token

##先构建一个random_ngram
def make_random_sentence(text_list,n): ###n>2
    ss_list = []
    sentence_list = []

    if n <= 2:
        print ("n should be equal to or more than 3")
    else:
        prob_dict = prob(text_list,n) ###创建字典
        prob_dict_sorted = dict(sorted(prob_dict.items(), key=lambda item:item[1], reverse=True))
        list_keys = list(prob_dict_sorted.keys())
        for key in list_keys:
            if key.split(" ")[:2] == ["<s>", "<s>"]:
                ss_list.append(key)
        random_head = random.choice(ss_list)
        sentence_list += random_head.split(" ")
        #print(sentence_list)
        i = 1
        while i <= 10-n:
            next_word = predict_next_word("".join(sentence_list[-(n-1):]),prob_dict_sorted,n)
            if next_word == "No words could be predicted!":
                i = i
            else:
                sentence_list.append(next_word)
                i += 1
        print("".join(sentence_list[2:]))


make_random_sentence(sentence_list1,3)