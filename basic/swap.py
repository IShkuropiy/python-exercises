
def main():
    nums = [1, 2, 3, 4, 5]
    a = 0
    b = len(nums) - 1

    if len(nums) > 1:
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

    print(nums)

main()

    # C++ avoid using a temp with exlusive or, xor
    # x = x xor y; 
    # y = y xor x;
    # x = x xor y;

