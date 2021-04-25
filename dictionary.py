import json
from difflib import SequenceMatcher
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        store= input("Did you mean %s instead! Enter Y if yes or N for no: " % get_close_matches(word,data.keys())[0])
        if store=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif store=="N":
            return "Word doesn't exist."
        else:
            return "We didn't understand your entry"
    else:
        return "Word doesn't exist."

word = input("Enter word: ")

output=translate(word)
if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)
