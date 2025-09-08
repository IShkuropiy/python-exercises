# Reverse a string
# Goal: Print the reverse of a string.
# Given: s = "python"
# Example output: nohtyp


def reverseStr(s):
    reverStr = ""

    reverStr = s[::-1] # [::-1] is the slicing operation. -1 is the step value. 

    print(reverStr)

def main():
    reverseStr("python")
    reverseStr("andrew loves apples")

main()