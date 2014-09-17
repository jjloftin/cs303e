def permute(a, lo):
  hi = len(a)
  if(lo == hi):
    print(a)
    return
  else:
    for i in range(lo, hi):
      a[lo], a[i] = a[i], a[lo]
      permute(a, lo + 1)
      a[lo], a[i] = a[i], a[lo]
def main():
  a = ['a','b', 'c', 'd']
  permute(a,0)
main()