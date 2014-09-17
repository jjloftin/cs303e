#check if two strings are anagrams ignoring case space and punctation

def isAnagram(a,b):
  a = a.lower()
  b = b.lower()
  
  for ch in a:
    if(ch.isalpha() and b.find(ch) == -1 ):
      return False
  for ch in b:
    if(ch.isalpha() and a.find(ch) == -1) :
      return False
  return True

def main():
  a = 'dog'
  b = 'G!o.    --==__D'
  print(a, b)
  print(isAnagram(a,b))
main()