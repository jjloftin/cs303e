#take in a 2D list reverse the rows
def reverseRows(a):
  for item in a:
    item.reverse()
  return a
def main():
  a = [[1,2,3],[4,5,6],[7,8,9]]
  print(reverseRows(a))
main()