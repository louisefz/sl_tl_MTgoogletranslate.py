from operator import itemgetter #useful for sorting a list by a specific item

# import json
# with open('/Users/zhoujie/Desktop/test/3gram_dict.json', 'r') as p:
#     js_str = p.read()
#     prob_dictionary_random = json.loads(js_str)
#     #print(prob_dictionary_random)
#     prob_dictionary = dict(sorted(prob_dictionary_random.items(), key=lambda item:item[1], reverse=True))
#
#
# def predict_next_5words(sentence):
#   gram2_list = sentence.split()[-2:]
#   list_tuple = []
#   try:
#     for key, value in prob_dictionary.items():
#      if key.split()[:-1] == gram2_list:
#       list_tuple.append((key.split()[-1],value))
#       result2 = list_tuple[:5]
#     return result2
#   except:
#     return "No words could be predicted!"
#
#
# print(predict_next_5words("to be"))



####绝对值
print(abs(-45))