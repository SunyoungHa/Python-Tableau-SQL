#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/python2.4 -tt

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    if len(s)>2:
        if s[-3:] == 'ing':
            return s + 'ly'
        else :
            return s + 'ing'
    else:
        return s

verbing ('tell')


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!



#googled 
def not_bad(s):
  snot = s.find('not')
  sbad = s.find('bad')

  if sbad > snot:
    s = s.replace(s[snot:(sbad+3)], 'good')

    # +3 means? 
  return s

not_bad('This dinner is not that bad!')




# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a,b):
    
    a_middle = len(a) // 2
    b_middle = len(b) // 2
    if len(a) % 2 == 1: # add 1 if length is odd
        a_middle = a_middle + 1
    if len(b) % 2 == 1:
        b_middle = b_middle + 1 
    return a[:a_middle] + b[:b_middle] + a[a_middle:] + b[b_middle:]

front_back('abcd','efgh')


#answer2

def front_back(a, b):
    hlena, hlenb = (len(a) + 1)//2, (len(b) + 1)//2
    return a[:hlena] + b[:hlenb] + a[hlena:] + b[hlenb:]

front_back ('abcd', 'edghi')


#answer3

def front_back(a, b):
    if len(a)%2==0:
        a_front = a[:len(a)//2]
        a_back = a[len(a)//2:]
    if len(b)%2==0:
        b_front = b[:len(b)//2]
        b_back = b[len(b)//2:]
        
    else :
        a_front = a[:(len(a)//2)+ 1]
        a_back = a[(len(a)//2)+1:]
        b_front = b[:(len(b)//2)+ 1]
        b_back = b[(len(b)//2)+1:]
    
    return a_front + b_back + b_front + a_back

test(front_back('abcd', 'xy'), 'abxcdy')


# G. Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
 # systext error : print(('%s got: %s expected: %s' % (prefix, repr(got), repr(expected))))
 #simpleString = '1+2'
 #print(simpleString) # 1+2
#print(str(simpleString)) # 1+2
#print(repr(simpleString)) # '1+2'
    
    

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print(('%s got: %s expected: %s' % (prefix, got, expected)))
test ('a', 'b')


# H. main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.

def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()


# In[ ]:




