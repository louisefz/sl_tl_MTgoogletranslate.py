

import re
import sys
import json

file = open("/Users/zhoujie/Documents/python2/1/fradulent_emails_utf8.txt", "r").read()

### Make a list of emails (full e-mail ass a single string) from the contents of the given document
### How can we access e-mails separately in a document of all e-mails? (Tip: Use re.split())
split_contents = re.split('From r ', file[0:30000])
list1 = []
contents = []
for ind, x in enumerate(split_contents):
    if x != '':
        list1.append(x)
        #print(ind)
#print(list1)
for y in list1:
    z = "From r " + y + "From r"
    contents.append(z)
#print(contents)

list_email_dict = []  # This is where we will store individual email dictionaries
counter = 0
for email in contents:
    counter += 1
    print("EMAIL COUNT = " + str(counter))

    ### Step 1: Create an empty dictionary for each email
    dict_email = {}
    ### Step 2: Get the sender name and address
    regrex_sender = '\nFrom: (.*)\n'
    dict_email['sender'] = "".join(re.findall(regrex_sender, email))

    ### Step 3: Get the receiver name and address
    regrex_receiver = '\nTo: (.*)\n'
    dict_email['receiver'] = "".join(re.findall(regrex_receiver, email))

    ### Step 4: Get date_sent
    regrex_date = 'From r  (.*)'
    dict_email['date'] = "".join(re.findall(regrex_date, email))

    ### Step 5: Get the subject of the e-mail
    regrex_subject = '\nSubject: (.*)\n'
    dict_email['subject'] = "".join(re.findall(regrex_subject, email))

    ### Step 6: Get the body of the e-mail (where does the body of each e-mail start?)
    regrex_body = "Status:.*\n*((.*\n)*?).*From r"
    body_list = re.findall(regrex_body, email)
    print("答案：", body_list)
    list_aux = []
    for tuple in body_list:
        list_aux.append(tuple[0])
    dict_email['body'] = "".join(list_aux)

    ### Step 7: Add all the information to the e-mail dictionary
    print(dict_email)
    list_email_dict.append(dict_email)
print(list_email_dict)
for dict in list_email_dict[0:5]:
    jsonx = json.dumps(dict)
    print(jsonx)