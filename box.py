# Hollow box with a custom border
# Goal: Print a hollow h × w rectangle with a border character ch.
# Given: w = 6, h = 4, `ch = '#'}
# Example output:

######
#    #
#    #
######


def fullRow(w, ch):
    print(ch * w)

def hollowRow(w, ch):
    print(ch + " " * (w - 2) + ch)

def Box(w, h, ch):
    fullRow(w, ch)

    for i in range(h - 2):
        hollowRow(w, ch)

    fullRow(w, ch) # not in the loop 

def main():
    Box(20, 4, "*")
    print("")
main()