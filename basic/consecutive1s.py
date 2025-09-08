# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# EX: Input: nums = [1,1,0,1,1,1] Output: 3

def ones(nums):
    maxCount = 0
    currentCount = 0

    for n in nums:
        if n == 1:
            currentCount +=1
            if currentCount > maxCount:
                maxCount = currentCount
        else:
            currentCount = 0

    return maxCount 

def main():
     ones1 = ones([1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1])
     print(ones1)
     ones2 = ones([])
     print(ones2)
     
main()