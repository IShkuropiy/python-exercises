# Write a function named armstrong_numbers that accepts an integer n as a parameter and prints all n-Armstrong numbers. An n-Armstrong number is a number containing exactly n digits where the sum of each digit raised to the nth power equals the number itself. For example, 153 is a 3-Armstrong number because 13 + 53 + 33 = 153. The call of armstrong_numbers(3) should print the following console output:

# 153 370 371 407
# If n is 0 or negative, or if there are no n-Armstrong numbers, print no output.

def readInt():

     while True:
        try:
            userIn = int(input("Enter an integer: "))
            print(f"{userIn} accepted.")
            return userIn
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def numToDigits(n):
    # Convert number to list of digits
    # return [int(ch) for ch in str(n)]

    if n == 0:
        return [0]

    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10

    digits.reverse()
    return digits

def isArmstrong(n):
    digits = numToDigits(n)
    power = len(digits)
    total = sum(d**power for d in digits)
    return total == n


def main():
    num = readInt()
    if isArmstrong(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is NOT an Armstrong number.")

main()