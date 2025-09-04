# Right triangle
# Goal: Print a right triangle of height h made of *.
# Given: h = 4
# Example output:
# *
# **
# ***
# ****

def triangle(h):
    i = 1
    result = []
    while i <= h:    
        result.append('*' * i)
        i += 1

    return '\n'.join(result)

def main():
  test1 = triangle((6))
  print(test1)
  test2 = triangle((12))
  print(test2)  
  test3 = triangle((0))
  print(test3)

main()