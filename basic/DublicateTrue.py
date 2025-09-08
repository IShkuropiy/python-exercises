# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from collections import defaultdict

def dup (s) -> bool:
    h = defaultdict(int)
    for i in s:
        h[i] += 1
        if h[i] > 1:
            return True        
    
    return False

def main ():

    s1 = dup([1,2,3,1])
    print(s1)

    s2 = dup([1,2,3,4])
    print(s2)

    s3 = dup([1,1,1,3,3,4,3,2,4,2])
    print(s3)

   
main()
