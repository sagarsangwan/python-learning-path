import json
import difflib 
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))
def translate(w):
        
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), ) )>0:
        yn = input("did u mean "+ ( get_close_matches(w, data.keys()) [0]) +(" y for yes or n for no : "))
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys()) [0]] 
        if yn == "n":
            return "please double check the word"
        else:
            return "sorry we did't understand your entry"
    else:
        return "please double check the word"
        
        
        
s = SequenceMatcher(None, "rain", "rainn").ratio()
word = input("enter a word: ")
output =translate(word)
if type(output) == list:
    for i in output:
        print(i)
