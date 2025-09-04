# Count vowels in a string
# Goal: Count how many vowels are in a string (vowels: aeiou), case-insensitive.
# Given: s = "Education" output 5

def vowels(s):
    result = 0
    vowels = "aeiou"

    for char in s.lower():
        if char in vowels:
            result += 1
    return result


def main():
    test1 = vowels("Education")
    print(test1)
    test2 = vowels("Internet")
    print(test2)
    test3 = vowels("aaaaaaAAaaaaa")
    print(test3)
main()

