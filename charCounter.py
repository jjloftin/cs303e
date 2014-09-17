#count the number of non-spaced characters in a string and print out a dictionary of their frequencies
def charCounter(st):
  freq_dict = {}
  st = st.replace(' ', '')
  
  for ch in st:
    if (ch in freq_dict):
      freq_dict[ch] += 1

    else:
      freq_dict[ch] = 1
      
  for key in freq_dict:
     print(key, freq_dict[key])
     
def main():
  charCounter('dog')
  charCounter('c     a                        t')
  charCounter('poopadoodle doo doo doo dee da do')
  
main()