# Goal: Print an h × w grid where cells alternate # and . like a checkerboard. Top-left is #.
# Given: w = 6, h = 4

#    #.#.#.
#   .#.#.#
#    #.#.#.
#.  .#.#.#

def checkers(w, h):
    for i in range(h):
        for j in range(w + 1):
            if (i + j) % 2 == 0:
                print("#", end="")
            else:
                print(".", end="")

        print("")
   

def main():
    checkers(6, 4)
    print("")
    checkers(5, 3)
    print("")
    checkers(12, 12)
    print("")
main()
