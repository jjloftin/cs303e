#take in a 2d list and reverse the columns

def colReverse(a):

  for j in range(len(a[0])):
    for i in range(len(a)//2):
      a[i][j], a[len(a) - 1 - i][j] = a[len(a) - 1 - i][j], a[i][j]
  return a
def main():
  a = [[1,2,3],[4,5,6],[7,8,9]]
  print(colReverse(a))
  
main()