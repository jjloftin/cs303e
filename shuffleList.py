import random

def shuffleList(a):
  c = a[:]
  b = []
  while(len(c) > 0):
    b.append(c[random.randint(0,len(c)-1)])
    c.remove(b[len(b)-1])
  return b

def main():
  a = [1, 5, 7, 9]
  print(a)
  print(shuffleList(a))
  print(shuffleList(a))

main()