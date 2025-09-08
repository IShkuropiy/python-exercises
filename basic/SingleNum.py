# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def findNum (s):
    # s = [2, 78, 0, 90, 3, 3, 78, 90, 0], 2
    s.sort() 
    
    i = 0
    
    while i < len(s):
        if i == len(s) - 1 or s[i] != s[i+1]:
            return s[i]
        i +=2
    

def main ():
    s1 = findNum([5, 787, 2, 2, 6, 5, 787, 6, 5, 3])
    print(s1)

    s2 = findNum([4,1,2,1,2])
    print(s2)

    s3 = findNum([1])
    print(s3)

main()
