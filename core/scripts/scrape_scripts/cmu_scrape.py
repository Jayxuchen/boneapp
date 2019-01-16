from bs4 import BeautifulSoup
import urllib3
import time

def getPronounciation(sentence):
    start = time.time()
    # print(time.strftime("%H:%M:%S", time.gmtime(time.time()-start)))
    base="http://www.speech.cs.cmu.edu/cgi-bin/cmudict?in="
    for word in sentence.split(" "):
        base+=word+"+"
	url=base[:-1]
	http = urllib3.PoolManager()
	response = http.request('GET', url)
	soup = BeautifulSoup(response.data, features='html.parser')
    text = soup.div.findAll()[-1].get_text()
    print(time.strftime("%H:%M:%S", time.gmtime(time.time()-start)))
    return text

print(getPronounciation("A dark rain cloud"))
