#!/usr/bin/env python
# coding: utf-8

# In[10]:


# I just practiced word count in several ways. It would be different from the quetion...

import re
import string
from sortedcontainers import SortedDict
frequency = {}
document_text = open('little_prince.txt', 'r')
text_string = document_text.read().lower()
match = re.findall(r'\w+', text_string)


 
for word in match:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()

for words in frequency_list:
    print (words, frequency[words])

# please help me to sort it


# In[9]:


#2 

fname = 'little_prince.txt'
lines =0
nwords =0
nchars =0
with open(fname,'r') as f:
        for line in f:
                word=line.split()
                lines+=1
                nwords+=len(word)
                nchars+=len(line)
print(nchars)
print(nwords)   


# In[28]:


#3

def count_lines(data):
    lines = data.split('\n')
    for l in lines:
        if len(l) == 0:
            lines.remove(l)
    return (len(lines))


# In[36]:


if __name__ == "__main__":
    filename = sys.argv[1]
    f=open('little_prince.txt','r')
    data = f.read()
    f.close()
    
    num_words = count_words(data)
    num_lines = count_lines(data)
 
    print("The number of words: ", num_words)
    print("The number of lines: ", num_lines)

   

