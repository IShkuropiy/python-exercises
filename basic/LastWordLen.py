# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

def lastWord(s):
    
    i = len(s) -1
    while i >= 0 and s[i] == ' ':
        i -= 1
    
    l = 0

    while s[i] != ' ' and i >= 0:
        i -= 1
        l += 1
    
    
    
    return l


def main():
    l1 = lastWord("    ")
    print(l1)

main()