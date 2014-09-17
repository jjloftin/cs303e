#  File: ISBN.py

#  Description: Assignmen 8. Open file of potential ISBN numers. Check their validity. Write results to an output file.

#  Student Name: Johnathon Loftin

#  Student UT EID: jjl2328

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: July 28th, 2014

#  Date Last Modified: July 30th, 2014


#checks if isbn is valid, returns boolean
def isbnValid(str):

  isbn = []
  
  #converts all characters to upper case [easier to check the check digit: can be either 'x' or 'X"]
  str = str.upper()
  
  #iterate through a potential ISBN, if invalid character found function returns false, also appends valid, non-hyphen characters to a list 
  for i in range(len(str)):
    if((str[i] != 'X') and (str[i] != '-') and ((ord(str[i]) < 48) or (ord(str[i]) > 57))):
      return False
    
    #X can only appear as the check character, not in the preceding digits
    if((i != len(str) - 1) and (str[i] == 'X')):
      return False
    
    #append only the digits and the check digit to the list
    elif((ord(str[i]) >= 48) and (ord(str[i]) <= 57)):
      isbn.append(eval(str[i]))
    
    elif(str[i] == 'X'):
      isbn.append(10)
       
        
  #check the length, if isbn contains more or less than 10 digits [including X] it's invalid.
  if(len(isbn) != 10):
    return False
    
    
  #now take the list isbn, and calculate its' first partial sum (nth term in sequence is sum of terms n, n-1, ..., 0)
  #then take the second partial sum (the partial sum of the first partial sum)
  s1 = [ ]
  s2 = [ ]
  
  for i in range(len(isbn)):
    s1.append(0)
    s2.append(0)
    
    #calculates the firat partial sum
    for j in range(i+1):
      s1[i] += isbn[j]
    
    #calculates the second partial sum
    for j in range(i+1):
      s2[i] += s1[j]
    
    
  #if s2[9] is divisible by 11 the ISBN is valid
  #print(s2[9] % 11)
  
  return (s2[9] % 11 == 0)
  
      
 
#takes input file, checks each ISBN in each line, writes to output
def main():

  #open unvalidated ISBN input file and validated ISBN output vile
  unchecked_isbns = open('isbn.txt', 'r')
  checked_isbns = open('isbnOut.txt', 'w')
  
  #check for validity of ISBNS in input file, write to output file. 
  for line in unchecked_isbns:
    if(isbnValid(line.strip())):
      checked_isbns.write(line.strip() + '  valid\n')
    else:
      checked_isbns.write(line.strip() + '  invalid\n')
  
  #close input and output
  unchecked_isbns.close()
  checked_isbns.close()
  
main()