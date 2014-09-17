#  File: DNA.py

#  Description: Assignment 7. Take an input file with n pairs of strings. Print the longest common substrings of length 2 or greater in those pairs

#  Student Name: Johnathon Loftin   

#  Student UT EID: jjl2328

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: July 25th, 2014

#  Date Last Modified: July 26th, 2014


def main():

  #open the text file of dna strands
  dna_strands = open('dna.txt', 'r')
  
  #extract the first line which contains the number of pairs to be analyzed
  num_pairs = eval(dna_strands.readline())


    
  
  #iterate through the file pair by pair printing the longest shared sequneces (neglect 1-character substrings)  
  print('\nLongest Common Sequences \n')

  for n in range(1, num_pairs + 1):
    #extract pair of strings from input file. Put it into upper case letters and extract extra spaces and EOL characters
    s1 = dna_strands.readline().upper().strip()
    s2 = dna_strands.readline().upper().strip()

    #check all of the shorter string's substrings, then store the longest substrings also found in the longer substring in a list
    
    #list to store substrings
    longest_subs = [ ]
    
    #if the second of the strings is longer
    if(len(s2) > len(s1)):
    
      #the length of the matching substring + iterator for outer loop
      sub_length = len(s1)
      
      while(sub_length > 1):
      
        #check to see if set of largest substrings found, break from loop if non-empty
        if(len(longest_subs) > 0):
          break
        
        #starting index for substrings of length = sub_length, iterator for inner loop
        index = 0   
   
        while(sub_length + index <= len(s1)):
          #if substring of length = sub_length found in longer string, append it to list of longest substrings
          if(s2.find(s1[index: index + sub_length]) > -1):
            longest_subs.append(s1[index: index + sub_length])
            
          index += 1
         
        sub_length -= 1  

    #if the first of the two strings is longer or the same length as the second: do the same as above but flip the roles for each string
    else:
      sub_length = len(s2)
      
      while(sub_length > 1):
        if(len(longest_subs) > 0):
          break
          
        index = 0
        
        while(sub_length + index <= len(s2)):
          if(s1.find(s2[index: index + sub_length]) > -1):
            longest_subs.append(s2[index: index + sub_length])
            
          index += 1
          
        sub_length -= 1
        
        
        
        
      
    #print out results
    
    s = 'Pair ' + str(n) + ': '
    prefix = len(s) * ' '
    
    print(s, end = '')
    
    if(len(longest_subs) == 0):
      print('No Common Sequence Found \n')
    
    else:
      for i in range(len(longest_subs)):
        if (i == 0):
          print(longest_subs[i])
        else:
          print(prefix + longest_subs[i])
      print('')
    
     
        
  #close input text file
  dna_strands.close()
  
  
main()