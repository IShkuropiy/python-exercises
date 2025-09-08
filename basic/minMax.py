#Find min and max (no built-ins)
# Goal: Print the smallest and largest values without using min()/max().
# Given: nums = [9, -2, 0, 11, 4]
# Example output: min = -2, max = 11

def findMin(nums):
    min = 0

    for n in nums:
        if n < min:
            min = n

    return min

def findMax(nums):
    max = 0

    for n in nums: 
          if n > max:
           max = n 

    print("min =", min, ", max =", max )

def minMax(nums):
    min = max = nums[0]

    for n in nums:
        if n > max:
            max = n
        if n < min:
            min = n
    return min, max

def main():
    min, max =  minMax([9, -2, 0, 11, 4])
    print("min =", min, ", max =", max )

main()


