def sortList(a):
  b = []
  
  while(len(a)>0):
    min = a[0]
    for item in a:
      if(item < min):
        min = item
    b.append(min)
    a.remove(min)
  return b

def main():

  a = [1,5,3,7,6,6,1,2]
  print(a)
  print(sortList(a))

main()