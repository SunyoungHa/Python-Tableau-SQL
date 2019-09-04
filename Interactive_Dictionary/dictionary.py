import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title()in data:
        return[word.title()]
    elif word.upper()in data:
        return[word.upper()]

    elif len(get_close_matches(word, data.keys()))>0:
        yesNo= input("Did you mean %s instead? Enter Yes or No." %get_close_matches(word,data.keys())[0])
        if yesNo == "yes":
            return data[get_close_matches(word,data.keys())[0]]
        elif yesNo == "no":
            return "Try again"
    else: 
        return "The word does not exist"

word = input("Enter word:")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print (output)

