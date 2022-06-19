import nltk
from nltk.corpus import gutenberg
import json
from operator import itemgetter
from collections import Counter
nltk.download('punkt')

dict_3 = {'martin , whom': 1.0, 'whom emma well': 0.33333, 'emma well knew': 1.0, 'well knew by': 1.0, 'knew by character': 1.0, 'by character ,': 1.0, 'character , as': 0.5, ', as renting': 0.07143, 'as renting a': 1.0, 'renting a large': 1.0, 'a large farm': 0.5, 'large farm of': 1.0, 'farm of mr': 1.0, 'knightley , and': 0.125, ', and residing': 0.00813, 'and residing in': 1.0, 'residing in the': 1.0, 'the parish of': 0.5, 'parish of donwell': 1.0, 'of donwell --': 1.0, 'donwell -- very': 1.0, '-- very creditably': 1.0, 'very creditably ,': 1.0, 'creditably , she': 1.0, ', she believed': 0.125, 'she believed --': 1.0, 'believed -- she': 1.0, '-- she knew': 1.0, 'she knew mr': 0.2, 'knew mr .': 1.0, '. knightley thought': 0.05882, 'knightley thought highly': 1.0, 'thought highly of': 1.0, 'highly of them': 1.0, 'of them --': 0.5, 'them -- but': 1.0, '-- but they': 0.25, 'but they must': 1.0, 'they must be': 1.0, 'must be coarse': 0.11111, 'be coarse and': 1.0, 'coarse and unpolished': 1.0, 'and unpolished ,': 1.0, 'unpolished , and': 1.0, 'and very unfit': 0.33333, 'very unfit to': 1.0, 'unfit to be': 1.0, 'be the intimates': 0.33333, 'the intimates of': 1.0, 'intimates of a': 1.0, 'of a girl': 0.04545, 'a girl who': 0.5, 'girl who wanted': 1.0, 'who wanted only': 1.0, 'wanted only a': 1.0, 'only a little': 0.5, 'a little more': 0.2, 'little more knowledge': 1.0, 'more knowledge and': 1.0, 'knowledge and elegance': 1.0, 'and elegance to': 1.0, 'elegance to be': 1.0, 'to be quite': 0.05, 'be quite perfect': 1.0, 'quite perfect .': 1.0, 'perfect . </s>': 1.0, '<s> _she_ would': 1.0, '_she_ would notice': 1.0, 'would notice her': 1.0, 'notice her ;': 1.0, 'her ; she': 0.5, '; she would': 0.5, 'she would improve': 0.2, 'would improve her': 1.0, 'improve her ;': 1.0, 'she would detach': 0.2, 'would detach her': 1.0, 'detach her from': 1.0, 'her from her': 0.33333, 'from her bad': 1.0, 'her bad acquaintance': 1.0, 'bad acquaintance ,': 1.0, 'acquaintance , and': 1.0, ', and introduce': 0.00813, 'and introduce her': 1.0, 'introduce her into': 1.0, 'her into good': 0.5, 'into good society': 1.0, 'good society ;': 1.0, 'society ; she': 1.0, 'she would form': 0.2, 'would form her': 1.0, 'form her opinions': 1.0, 'her opinions and': 1.0}
predicted_gram_dict = dict(sorted(dict_3.items(), key=lambda item:item[1], reverse=True))
#print(predicted_gram_dict)
dict_2 = {'martin ,' : 1.0, 'whom emma': 0.33333, 'emma well': 1.0, 'well knew by': 1.0, 'knew by': 1.0, 'by character': 1.0, 'character ,': 0.5}



sentence = "martin,"
gram2_list = nltk.word_tokenize(sentence)[-2:]
list_tuple = []
for key, value in predicted_gram_dict.items():
    if key.split()[:-1] == gram2_list:
        list_tuple.append((key, value))
        print(dict_2.items())
    else:
        print(0)





