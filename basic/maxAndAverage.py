# Sum and average
# Goal: Print the sum and average of numbers in a list.
# Given: nums = [3, 5, 2, 8]
# Example output: sum = 18, avg = 4.5

def findSum(nums):
    sum = 0
    count = 0

    for n in nums:
        sum += n
        count += 1

    return sum 

def findAverage(nums):
        sum = 0
        count = 0
        avg = 0
        
        avg = sum / count
        print("sum =", sum, ", avg =", avg )

def main():
    findSum([3, 5, 2, 8])
    findAverage([3, 5, 2, 8])
main()