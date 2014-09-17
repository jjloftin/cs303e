#take in two 1d lists and return the dot product
def dotLists(a,b):
  sum = 0
  for i in range(len(a)):
    sum += a[i]*b[i]
  return sum
  
def main():
  a = [1, 1, 1]
  b = [1, 5, 5]
  print(dotLists(a,b))

main()