#function that sums two lists of equal size

def sumList(a,b):

  for i in range(len(a)):
    for j in range(len(a[i])):
      b[i][j] = a[i][j] + b[i][j]
  return b

def main():
  print(sumList([[1,2,3], [4,5,6]], [[1,2,3],[4,5,6]]))
main()