# Main diagonal
# Goal: Print an n × n grid with \ on the main diagonal and . elsewhere.
# Given: n = 5
# Example output:

# \....
# .\...
# ..\..
# ...\.
# ....\


def diagonal(n):
    for i in range(n):
        print( "." * i + "\\" + "." * (n - i - 1))

def main():
    diagonal(5)
    print("")
main()