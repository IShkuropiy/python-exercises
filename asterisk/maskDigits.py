# Mask digits
# Goal: Replace every digit in a string with #, leave other characters unchanged.
# Given: s = "Room 101: 7 guests"
# Example output: Room ###: # guests

def maskDigits(s):
    digits = "0123456789"
    strBuild = [] # string builder, pattern in work with a strs
    for char in s:
        if char in digits:
            strBuild.append("#")
        else:
            strBuild.append(char)
            
    return  "".join(strBuild)

def main():
        test1 = maskDigits("She born in 1992")
        print(test1)
        test2 = maskDigits("2r473853465894369236")
        print(test2)
        test3 = maskDigits("sdfjksdgfjsakghdfkja")
        print(test3)

main()
