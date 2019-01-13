from bs4 import BeautifulSoup
import urllib3


def getPronounciation(sentence):
    base="http://www.speech.cs.cmu.edu/cgi-bin/cmudict?in="
    for word in sentence.split(" "):
        base+=word+"+"
    url=base[:-1]
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response, 'html.parser')
    soup = BeautifulSoup(response.data)
    tt = soup.findAll("div", class_= "")
    print(tt)

getPronounciation("this")
