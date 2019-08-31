import re, operator

# keys are words, vals are occurance frequency
freqlist={}

f = open("/Users/sunyoungha/Downloads/little_prince.txt", "r", encoding="utf-8")
s=f.read()
f.close()

s=s.lower()

wordlist = re.split(r'\W',s);

for wd in wordlist:
     if wd in freqlist:
         freqlist[wd]=freqlist[wd]+1
     else:
         freqlist[wd]=1

for k,v in sorted(freqlist.items(), key=operator.itemgetter(1) ,reverse=True):
    print(str(v) + " → " + k)