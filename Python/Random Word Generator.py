import requests
import random 

# Global variables
word_list_URL = 'https://www.mit.edu/~ecprice/wordlist.10000' # wordlist of 10000 words

def getRandomWord():
    words = getWordRequest()
    random.shuffle(words)
    return random.choice(words)
    
def getWordRequest():
    try:
        response = requests.get(word_list_URL)
        words = response.content.splitlines()
        return words
    except:
        raise RuntimeError

print(getRandomWord())