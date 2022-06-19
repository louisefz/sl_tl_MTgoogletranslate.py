import json
with open('/Users/zhoujie/Desktop/test/3gram_dict.json', 'r') as p:
    js_str = p.read()
    prob_dictionary_random = json.loads(js_str)
    print(prob_dictionary_random)
    prob_dictionary = dict(sorted(prob_dictionary_random.items(), key=lambda item:item[1], reverse=True))


def predict_next_word(sentence,prob_dict,n): ###例如用3——gram词典来进行输入，则需要找到一个
  gram2_list = sentence.split()[-(n-1):]  #这里是2
  list_tuple = []
  try:
    for key, value in prob_dict.items():
     if key.split()[:-1] == gram2_list: #这里是
      list_tuple.append((key.split()[-1],value))
      result2 = list_tuple[0]
    return result2
  except:
    return "No words could be predicted!"
#print(predict_next_word("to be",predicted_gram_dict3,3))