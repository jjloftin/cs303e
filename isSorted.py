#returns true if 1d list sorted in ascending order, false if not

def isSorted(a):
  for i in range(len(a)-1):
    if(a[i] > a[i+1]):
      return False
  return True
  
def main():
  print(isSorted([1,2,3,4,5]))
  print(isSorted([1,3,7,9,13,21,63,174,999]))
  print(isSorted([1,2,3,4,4,4,4,3]))
main()