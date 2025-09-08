# Vowel count per word (nested over list + chars)
# Goal: For each word, print the word and how many vowels it contains.
# Given: words = ["code", "loop", "string"]
# Example output: code: 2, loop: 2, string: 1

def count(s):
    word = ""
    vowels = "aeiou"
    count = 0

    for c in s.lower():
        if c in vowels:
            count += 1
    return count

def countPerWord(words):
    for w in words:
        n = count(w)
        print(f"{w}: {n}")

def main():
    countPerWord(["code", "loop", "string"])
main()