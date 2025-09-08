# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.
# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.
# its already sorted 
# three pointers 

from collections import defaultdict 

def findIntersection(nums1, nums2, nums3):
    
    h = defaultdict(int)
    result = []

    for k in nums1:
        h[k] += 1

    for k in nums2: # for each element k in the nums2 list, 
        h[k] +=1    # value associated with the key k in the dictionary h is incremented by 1
                     # a check is performed to determine if k has appeared more than once
          

    for k in nums3: 
        h[k] +=1
        if h[k] == 3:
            result.append(k)

    return result

def main():
    test = findIntersection([1, 2, 3, 56, 78, 90, 0], [34, 56, 78, 90, 0, 1], [90, 12])
    print(test)

main()