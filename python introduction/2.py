import spacy
nlp = spacy.load("en_core_web_sm")
text = "The black dog sleeps and the red dog sleeps."
doc = nlp(text)
list11 = []
#我的方法
for candidate1 in doc:
  if candidate1.dep_ == "amod" and candidate1.head.pos_ == "NOUN":
    if candidate1.head.dep_ == "nsubj" and candidate1.head.head.pos_ == "VERB":
      list11.append((candidate1, candidate1.head.head))
print(list11)
#老师的方法
for candidate1 in doc:
  if candidate1.dep_ == 'nsubj' and candidate1.head.pos_ == 'VERB':
    for child in candidate1.children:
      if child.pos_ == 'ADJ' and child.dep_ == 'amod':
        print((child.text, candidate1.head.text))



