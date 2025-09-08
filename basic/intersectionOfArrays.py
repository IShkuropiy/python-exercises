# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

from collections import defaultdict

def findIntersection(nums1, nums2):
    h = defaultdict(int)
    result = []

    for k in nums1:
        h[k] = 1

    for k in nums2:
        h[k] +=1
        if h[k] > 1:
            result.append(k)

    return result

def main():

    test1 = findIntersection([11, 11, 11, 5, 6, 11 ], [2, 5, 11, 6, 4])
    print(test1)

main()