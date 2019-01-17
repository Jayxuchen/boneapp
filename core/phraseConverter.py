#!/usr/bin/python3
import requests
import sys
from bs4 import BeautifulSoup
import urllib3
import re
import MySQLdb
import configparser

# web scrapes the CMU Dictionary website
config = configparser.ConfigParser()
config.read("db.conf")
user = config['CREDENTIALS']['user']
passw = config['CREDENTIALS']['pass']
db = config['CREDENTIALS']['db']
host = config['CREDENTIALS']['host']
cnx = MySQLdb.connect(user=user, password=passw,host=host, db=db)
def getPronounciation(sentence):
	print("start")
	cursor = cnx.cursor()
	# print(sentence)
	sentence = sentence.strip().split(" ")
	ret = ''
	for word in sentence:
		query = "SELECT pronunciation FROM words WHERE word=%s"
		cursor.execute(query,(word.upper(),))
		ret+=cursor.fetchone()[0]+" . "

	print("end")
	# cursor.close()
	# cnx.close()
	return ret.strip()
# adjusts the sounds of words
def changeSounds(inputString):
	#print(inputString)
	changedClusters = {	"aa" : " a",
						"ae" : " a",
						"ah" : " uh",
						"ao" : " aw",
						"aw" : " ou",
						"ay" : " ie",
						"dh" : " th",
						"iy" : " ee",
						"hh" : " h",
						"ey" : " ay",
						"jh" : " jj",
						"ow" : " oa",
						"uh" : " oo",
						"uw" : " oo"
					}
	old = 0
	tempString = ""
	firstLetter = True
	while old != -1:
		new = inputString.find(' ', old+1) #takes the index of the next space
		if new != -1:

			if (firstLetter and new - old == 2 and inputString[old:new] in changedClusters) or (not firstLetter and new - old == 3 and inputString[old+1:new] in changedClusters):

				if firstLetter:
					tempString += changedClusters.get(inputString[old:new])
				else:
					tempString += changedClusters.get(inputString[old+1:new])
			else:
				tempString += inputString[old:new]
			old = new
		else:
			tempString += " ."
			old = -1
		firstLetter = False

	#print(tempString)
	return tempString

# first change of splitting up the letters in the words differently
def splitWords(inputString):
	newString = inputString
	if newString.find(' ') == -1:
		sys.exit("no spaces in phonetic string, word is weird 1")

	index = newString.find(' ', newString.find(' ')+1)
	if index == -1:
		sys.exit("no spaces in phonetic string, word is weird 2")

	index = 0

	vowelReached = False
	vowels = ['a','e','i','o','u','y'] #included 'y' in vowels
	newString = newString.lower()
	newString = newString.replace(". ", "")
	newString = newString.replace("  ", " ")

	if newString[0] in vowels:
		vowelReached = True
		index = newString.find(' ')

	while index != -1:
		while index != -1 and newString[index+1] in vowels: #if the next character is a vowel, check if the next cluster also starts w/ vowels. if so, loop through again until the next cluster starts w/ a consonant
			vowelReached = True
			index = newString.find(' ', index+1)

		index = newString.find(' ', index+1) #takes the index of the next space

		if vowelReached and newString[index+1] != '.': #if a vowel has been reached and the index is not at the end of the string, insert a period.
			newString = newString[:index] + " ." + newString[index:]

		vowelReached = False #reset vowelReached variable for every loop

	return newString

def checkSplitsForRepetition(inputString, splitString):
	tempInputString = inputString
	tempSplitString = splitString
	tempInputString = tempInputString.lower().replace("  ", " ").replace("aa", "a")

	originalWordArr = buildWordList(tempInputString)
	newWordArr = buildWordList(tempSplitString)

	#print(originalWordArr)
	#print(newWordArr)

	vowels = ['a','e','i','o','u','y'] #included 'y' in vowels

	ind = 0

	for indexNew in range(len(newWordArr)):
		for indexOld in range(len(originalWordArr)):
			if originalWordArr[indexOld][0] == newWordArr[indexNew][0]:
				if originalWordArr[indexOld][1] - indexOld == newWordArr[indexNew][1] - indexNew:
					if indexNew != 0 and newWordArr[indexNew][0][1] in vowels:
						ind = splitString.rfind(' ', 0, newWordArr[indexNew][1] - 2)
						if ind != -1:
							splitString = splitString[:ind] + " . " + splitString[ind+1:newWordArr[indexNew][1] - 2] + splitString[newWordArr[indexNew][1]:]
					elif indexNew != 0 and newWordArr[indexNew][0][1] not in vowels:
						ind = splitString.find(' ', newWordArr[indexNew][1]+1)
						if ind != -1:
							splitString = splitString[:newWordArr[indexNew][1]-2] + splitString[newWordArr[indexNew][1]:ind] + " . " + splitString[ind+1:]

	#print(splitString)
	return splitString

# input: a string of words separated by periods
# output: an array of words
def buildWordList(phrase):
    words = []        # add sounds one by one into this words list, empty list for now
    temp = ""
    counter = 0
    prevIndex = counter
    for c in phrase:    # assumes phrase has a period at the end of the string
        if c == '.':
            cluster = [temp, prevIndex]
            words.append(cluster)
            prevIndex = counter+1
            temp = ""
        else:
            temp += c
        counter += 1
    return words


def printList(ll):
	s = ""
	for x in ll:
		s += x + " "
	return s

# input: a string (sound)
# output: the top string with frequency (f) above 3.5
def apicall(x):
	payload = {'sl': x, 'md': 'f'}
	r = requests.get("https://api.datamuse.com/words", params = payload)
	jdata = r.json()
	for x in jdata:
		frequency = float(x["tags"][0][2:])
		if (frequency > 2):
			return x["word"]
	return "error"

# input: an array of words (sounds)
# output: an array of words (real dictionary words)
def realWords(words):
	newWords = []
	for x in words:
		newWords.append(apicall(x))
	# need to check against the original words inputted, cannot be the same
	return newWords

# input: phonetic sound, already put into CMU
# output: mad gab phrase
def convert(inputPhrase):
	inputPhrase = inputPhrase.lower()
	inputPhrase = changeSounds(inputPhrase)

	phrase = inputPhrase
	phrase = splitWords(inputPhrase)     # shirlyn's function to rearrange the periods and split up the sounds differently
	phrase = checkSplitsForRepetition(inputPhrase, phrase)

	phrase = phrase.replace(" ", "")
	words = realWords(phrase.strip(".").split("."))
	return printList(words)

def phraseConvert(phrase):
	phoneticPhrase = getPronounciation(phrase)
	madGabPhrase = convert(phoneticPhrase)
	return madGabPhrase

if __name__ == "__main__":
	phrase = input("Enter your phrase: ")
	print(phraseConvert(phrase))
