# Write a function named ascii_figure that draws a figure of the following form, using for loops.
# ////////////////\\\\\\\\\\\\\\\\
# ////////////********\\\\\\\\\\\\
# ////////****************\\\\\\\\
# ////************************\\\\
# ********************************

def figure(w, h):

    for i in range(h):
        f = int(w / 2 - i * w / h / 2)

        print("/" * f + "*" * (w - 2 * f) + "\\" * f)

def lines(s):
    print("/" * 16 + "\\" * 16, end="")
    print("")

def linesAndAst(s):
    print("/" * 12 + "*" * 8 + "\\" * 12, end="")
    print("")

def linesAndAst2(s):
    print("/" * 8 + "*" * 16 + "\\" * 8, end="")
    print("")

def linesAndAst3(s):
    print("/" * 4 + "*" * 24 + "\\" * 4, end="")
    print("")

def asteriks(s):
    print("*" * 32, end="")
    print("")

def main():
    lines(32)
    linesAndAst(32)
    linesAndAst2(32)
    linesAndAst3(32)
    asteriks(32)

    print("")

    figure(60, 10)
main()

