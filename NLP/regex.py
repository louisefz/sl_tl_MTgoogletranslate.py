
# 1. How would you search for a line containing at least two times the word “book”?  Steps for this question are as follows:
'''
(1) SpaCy will be used to segment one text into sentences;
(2) Each sentence is to be lemmatized;
(3) Loop each sentence, and in each sentence, we can use regrex to find all "book" or "books";
(5) The list for lemmatized "book" will be formed, and count all "book" in the list;
(6) If the number of count is more than 1, the sentence will be printed.
'''
import re
import spacy
text1 = """A book are good for people, and therefore people should read more books and buy a book. She is reading a book, and this book is recommended by his father. Cat dog Queen are a British rock band formed in London in 1970. Their classic line-up was Freddie Mercury (lead vocals, piano), Brian May (guitar, vocals), Roger Taylor (drums, vocals) and John Deacon (bass). Their earliest works were influenced by progressive rock, hard rock and heavy metal, but the band gradually ventured into more conventional and radio-friendly works by incorporating further styles, such as arena rock and pop rock.\nBefore forming Queen, May and Taylor had played together in the band Smile. Mercury was a fan of Smile and encouraged them to experiment with more elaborate stage and recording techniques. He joined in 1970 and suggested the name "Queen". Deacon was recruited in February 1971, before the band released their eponymous debut album in 1973. Queen first charted in the UK with their second album, Queen II, in 1974. Sheer Heart Attack later that year and A Night at the Opera in 1975 brought them international success. The latter featured "Bohemian Rhapsody", which stayed at number one in the UK for nine weeks and helped popularise the music video format."""
nlp = spacy.load('en_core_web_sm')
doc = nlp(text1)
for sentence in doc.sents:
    sentence_lemma = sentence.lemma_
    regrex1 = r'book'   ### r"^.* book .* book .*$"   boundary可加可不加
    q1 = re.findall(regrex1, sentence_lemma)
    count1 = q1.count("book")
    if count1 > 1:
        print(count1,sentence)


# 2. What will be returned by the query “fairplay|ness” ?
'''
The result of such query is a list which consists of "fairplay" and "ness".
#####One thing to be mentioned that if one word whose affix is "ness", "ness" of this word is to be queried and shown in the list.
'''

text2 = """fairplay is a digital rights management (DRM) technology developed by Apple Inc. fairnessness and justice are two elements which are important to people. ness is a kind of affix."""
regrex2 = r'fairplay|ness'
q2 = re.findall(regrex2, text2)
print(q2)


# 3. How would you substitute “08/02/2021” by “2021-02-08”?
text3 = """Today is 08/02/2021"""
regrex3 = r'08/02/2021'
q3 = re.sub(regrex3, "2021-02-08", text3)
print(q3)

# 4. Why can’t we use [cat|dog] if we want to search for either “cat” or “dog” in a text?
'''
The expression "[]" is to find the sigle character instead of words in sentences. Therefore, if we use "[cat|dog]", the single letters of "cat" and "dog" will be queried. 
If we need to find either "cat" or "dog", we can removed the square bracket"[]" and directly use "cat|dog".
'''

text4 = """cat is a kind of animal, and dog is cute."""
regrex4 = r'[cat|dog]'
q4 = re.findall(regrex4, text4)
print(q4)
text4a = """cat is a kind of animal, and dog is cute."""
regrex4a = r'cat|dog'
q4a = re.findall(regrex4a, text4a)
print(q4a)


# 5. How would you search for “baby” and the plural “babies” in a text?
text5 = """She was a cute baby, and now she has 2 cute babies. """
regrex5 = r'baby|babies'   #bab(y|ies)
q5 = re.findall(regrex5, text5)
print(q5)

# 6. How would you search for instances of “hello” and “Hello” and both variations with 3 digits (e.g. “hello123”, “Hello982”) in a text?
text6 = """Hello456, hello123, hello, Hello, hello764, hello13476134, hello1, Hello3764174"""
regrex6 = r'\bHello+[0-9][0-9][0-9]\b|\bhello+[0-9][0-9][0-9]\b' # regrex6 = r'\b(H|h)ello+[0-9][0-9][0-9]\b' can work on https://regex101.com/, but not work on pycharm. 或者直接\b(H|h)ello[0-9]{3}\b
q6 = re.findall(regrex6, text6)
print(q6)

# 7. How would you match all prices between €10 and €1001? (including decimal numbers)
# TIPS: 1) digits can be captured with \d and with [0-9], 2) use the “test_yourself” file on Ufora to test your solution.
text7 = """Cheese 1 kg. 11,3 - 34 USD = €10 - €30
fresh beef 22,7 - 28,3 USD = €22.7 per 1 kg
fresh pork 11,3 - 14,7 USD = €11.9 per 1 kg
smoked sausage 11,3 - 14,7 USD = €10.4 per 1 kg
sausages 7,9 - 10,2 USD = €8.9 EUR for 1 kg
Sausages for frying 300g. 4,8 USD = €4.2
bacon sliced 120g 3,2 USD = €2.8
Сhicken 1.13 kg. 4,9 USD = €4.3
0.7 kg of turkey fillet. 8,3 USD = €7.3
New PS4 gaming console = €410.4
2x New Playstation 5 Bundle = €1001.1
Used playstation games = €20.5 - €60.5
Volvo S90 B6 = €46508
Mazda 3 Hatchback Premium = €24948
Used Mini Oxford Edition = €10000
Oak Cabinet = €1000.2
Stained Drawers = €800.7
Glass Table = €1100.5"""
regrex7 = r'€[1-9]\d[.]\d\b|€[1-9]\d\b|€[1-9]\d\d[.]\d\b|€[1-9]\d\d\b|1000\b|€1000[.]\d\b|€1001[.][0]\b'
q7 = re.findall(regrex7, text7)
print(q7)


# 8. Can you think of a regex that could be implemented by a chat bot on a website like BOL.com? (e.g. after a complaint is made)
'''
(1) When users imput complaints in the chatbox, we will use urllib.request to get the content of the information from the webpage through API.
(2) We will process the information strings and turn them into tokens, lemmas, or some other forms that can be used acoording to the scenarios. 
(3) When we get the processed input informtion, we will use regrex to find all matched information in our corpus, and MED may be used to calculate the text similarity. 
(4) Once we find the best result in our corpora, we will print it, and send it to chatbox through API. 
(5) If there is no matched informtion in our corpora, we will return a default sentence. 
'''


























