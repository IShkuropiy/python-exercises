# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

def remove(nums, val):
    # nums = [2, 6, 45, 7, 8, 56, 4, 2, 34 , 5, 9 , 2]
    # val = 2
    # i started from 0, j from 12 . swap i & j if i = val
    # k = len(nums) after removing all val. 
    # for k in nums:
    #if k != val
    # k = len(nums)
    if len(nums) == 0:
        return 0
    
    i = 0
    j = len(nums) -1

    while i < j:
        if nums[i] == val:
            # replacement of nums[i]
            while i < j and nums[j] == val:
                j -= 1
            nums[i] = nums[j]# if we found val we decrese j
            j -= 1
        else:
            i += 1
    # end while
        
    if nums[i] != val:
        return i + 1
    else:    
        return i


def main():
    k1 = remove([5, 3, 2, 6, 3], 3)
    print(k1)

    k2 = remove([5, 3, 3, 6, 3], 3)
    print(k2)

    k3 = remove([], 0)
    print(k3)

    k4 = remove([3, 3, 3], 3)
    print(k4)


main()

