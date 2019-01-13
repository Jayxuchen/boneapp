import requests
import sys
from bs4 import BeautifulSoup
import urllib3

def getPronounciation(sentence):
    base="http://www.speech.cs.cmu.edu/cgi-bin/cmudict?in="
    for word in sentence.split(" "):
        base+=word+"+"
    url=base[:-1]
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, features='html.parser')
    text = soup.div.findAll()[-1].get_text()
    return text

def splitWords(inputString):
	#print("FUNC: splitWords")
	newString = inputString
	print(newString)
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

	newString = newString.replace("aa", "a") #takes out double a's

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

	#newString = newString.replace(" ", "") # these two lines get rid of excess whitespace
	#"".join(newString.split())

	return newString
    

def printList(ll):
    for x in ll: 
        print(x, end = " ")
    print()

# input: a string (sound)
# output: the top string with frequency (f) above 3.5
def apicall(x):
    payload = {'sl': x, 'md': 'f'}
    r = requests.get("https://api.datamuse.com/words", params = payload)
    jdata = r.json()
    for x in jdata:
        frequency = float(x["tags"][0][2:])
        if (frequency > 3.5): 
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
def convert(phrase):
    phrase = splitWords(phrase)     # shirlyn's function to rearrange the periods and split up the sounds differently
    phrase = phrase.replace(" ", "")
    words = realWords(phrase.strip(".").split("."))
    printList(words)

if __name__ == "__main__":
    phrase = input("Enter your phrase: ")
    phoneticPhrase = getPronounciation(phrase)
    madGabPhrase = convert(phoneticPhrase)