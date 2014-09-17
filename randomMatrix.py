import random

#make 2D list of size 3 x 5 with random numbers from 1 to 100
def randomMatrix():
  a = []
  for i in range(3):
    a.append([])
    for j in range(5):
      a[i].append(random.randint(1,10))
  return a
def main():
  print(randomMatrix())
  print('')
  print(randomMatrix())
main()