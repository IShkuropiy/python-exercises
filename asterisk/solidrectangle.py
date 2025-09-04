# Solid rectangle of stars
# Goal: Print a solid h × w rectangle of *.
# Given: w = 5, h = 3

def rectangle(w, h):
    i = 0
    j = 0
    row = ""
   
    for i in range(h):
        for j in range(w):
            print("*", end="")
        print("")
 

def main():
    rectangle(5, 3)
    print("")
    rectangle(4, 4)
    print("")
    rectangle(0, 4)
    print("")
    rectangle(0, 0)
    print("")

main()


