
import re
import MySQLdb
import configparser
import time

config = configparser.ConfigParser()
config.read("../../db.conf")
user = config['CREDENTIALS']['user']
passw = config['CREDENTIALS']['pass']
cnx = MySQLdb.connect(user=user, password=passw, host='127.0.0.1', db='boneapp')
cursor = cnx.cursor()

def getPronounciation(sentence):
    start = time.time()
    # print(time.strftime("%H:%M:%S", time.gmtime(time.time()-start)))
    sentence = sentence.strip().split(" ")
    ret = ''
    for word in sentence:
        query = "SELECT pronunciation FROM words WHERE word=%s"
        cursor.execute(query,(word.upper(),))
        ret+=cursor.fetchone()[0]+" . "
    cursor.close()
    cnx.close()
    print(time.strftime("%H:%M:%S", time.gmtime(time.time()-start)))
    return ret.strip()
print(getPronounciation("A dark rain cloud"))
