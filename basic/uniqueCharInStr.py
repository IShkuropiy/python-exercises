#  Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# s consists of only lowercase English letters.
# return second: skip iteraction of first or skip returning first 
from collections import defaultdict 

def findUniqueChar(s):
    h = defaultdict(int)
    letter = ''
    count = 0 # how many unique chars we will found
    result = -1

    for letter in s:
        h[letter] += 1

    for i in range (len(s)):
        if h[s[i]] == 1:
           count +=1 
           if count == 2:
              result = i
              break

    return result

def main():
    test = findUniqueChar("skasgaardswen")
    print(test)

main()