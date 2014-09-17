#take in two lists of strings, return a list of the strings common to both

def stringCommon(a, b):
  return set(a) & set(b)
  
def main():
  a = ['dog', 'cat', 'tweetwee', 'bones']
  b = ['cat', 'meow', 'milk']
  print(stringCommon(a,b))
  
main()