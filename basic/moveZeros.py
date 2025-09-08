# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
#Input: nums = [0,1,0,3,12] Output: [1,3,12,0,0]

def swap(nums, i, j):
    if (i >= 0 and i <= len(nums) -1) and (j >= 0 and j <= len(nums) -1):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

def getNextNonZero(nums, j):
    while j < len(nums):
        if nums[j] != 0:
            return j
        j += 1

    return j

def moveZeros(nums):
    j = 0
    for i in range (len(nums)):
        if nums[i] == 0:
            if j <= i:
                j = i + 1
            j = getNextNonZero(nums, j)
            swap(nums, i, j)
    
    return nums

def main():
    moveZeros1 = moveZeros([0, 0, 0, 0, 0, 0, 0, 0, 0, 67])
    print(moveZeros1)
main()