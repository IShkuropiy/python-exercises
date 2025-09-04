def triangle(h):
    i = 1
    result = []

    for i in range(1, h + 1):
       if i < h:
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
  test4 = triangle((4))
  print(test4)

main()