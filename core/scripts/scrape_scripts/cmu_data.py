import re
import mysql.connector
import configparser
#https://pleasval.org/wp-content/uploads/2017/12/2017-2018-school-spelling-bee-study-list-by-grade-watermark.pdf

#set up db credentials
config = configparser.ConfigParser()
config.read("db.conf")
user = config['CREDENTIALS']['user']
passw = config['CREDENTIALS']['pass']
cnx = mysql.connector.connect(user=user, password=passw, host='127.0.0.1', database='boneapp')
cursor = cnx.cursor()

word_fn = "words_8_dict.txt"
word_fp = open(word_fn)
# app_id = 'ca72a05b'
# app_key = '3a647523ee30ba81d7210fcf2ce10ac5'
# language = 'en'
# word_id = 'Ace'
for line in word_fp:
    line = re.split("\t",line.strip())
    word,pronunciation = line[0],line[1]
    word = re.sub(r'\(\d+\)','',word)
    # url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
    #
    # r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    #
    # print("code {}\n".format(r.status_code))
    # print("text \n" + r.text)
    # print("json \n" + json.dumps(r.json()))

    query = "INSERT into words VALUES (NULL,%s,%s,NULL,NULL)"
    print(query)
    cursor.execute(query,word,pronunciation)
cursor.close()
cnx.close()
