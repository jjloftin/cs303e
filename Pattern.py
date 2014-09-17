#  File: Pattern.py

#  Description: Assignment 1. The problem here is to print an X pattern specified in the given assignment. 
#  I solve this problem by using two 'while' loops that systematically prints each line to given specification
#  the benefit here is that this would be an easy program to change so an X pattern of any size could be printed with 
#  ease. Honestly, I just wanted to do something besides copying and pasting.

#  Student Name: Johnathon Loftin

#  Student UT EID: jjl2328

#  Course Name: CS 303E

#  Unique Number: 90110 

#  Date Created: June 13th, 2014

#  Date Last Modified: June 13th, 2014

############################################################################

#for ease of reference I copy the picture here
#
#     *************************
#     *  *******************  *
#     **  *****************  **
#     ***  ***************  ***
#     ****  *************  ****
#     *****  ***********  *****
#     ******  *********  ******
#     *******  *******  *******
#     ********  *****  ********
#     *********  ***  *********
#     **********  +  **********
#     *********  ***  *********
#     ********  *****  ********
#     *******  *******  *******
#     ******  *********  ******
#     *****  ***********  *****
#     ****  *************  ****
#     ***  ***************  ***
#     **  *****************  **
#     *  *******************  *
#     *************************

def main():
# Print blank lines as specified 
  print(' ')
  print(' ')

#iterator for the loop we are going to use. i will count the number of stars on the edge
#of the i+1'th line and the 20-i'th line
  i=1

#print the first line take note that there are 25 stars in this line
  print('     *************************')

#note that there are 20 lines in total

#this will print the first half of the picture
  while (i <= 9):

  #vsriable used to count the number of stars on the edges
    j = 1
 
  #string used to construct each line. With 5 spaces on the left side as specified.
    line= '     '
  
  #add the first stars of the i+1'th line
    while(j<=i):
      j = j + 1
      line = line + '*'
	
  #add the spaces after the first stars of the i +1'th line
    line = line + '  '
  
  #iterator used to determine the number of stars in the middle of the i+1'th line
    l = 21 - 2 * i
  
  #add the middle stars
  
    while(l > 0):
      l = l - 1
      line = line + '*'
    
	
  #add the spaces before the last stars on the i + 1'th line
    line = line + '  '

  #add the stars to the end of the line
    while(j > 1):  
      j = j - 1
      line = line + '*'
	
	
  #print the i+1'th line	
    print(line)	
    i = i + 1
  
#print the 10th line
  print('     **********  +  **********')

#set the iterator for to 9, otherwise the improper number of stars on each line will be printeds 
  i = 9

#This will basically do the exact same thing as the first part of the program just in reverse
  while (i >= 1):

  #vsriable used to count the number of stars on the edges
    j = i
 
  #string used to construct each line. With 5 spaces on the left side as specified.
    line= '     '
  
  #add the first stars of the 20-i'th line
    while(j > 0):
      j = j - 1
      line= line + '*'
	
  #add the spaces after the first stars of the i+1'th line
    line = line + '  '
  
  #iterator used to determine the number of stars in the middle of the 20-i'th line
    l = 21 - 2*i
  
  #add the middle stars
  
    while(l>0):
      l = l - 1
      line = line + '*'
    
	
  #add the spaces before the last stars on the 20-i'th line
    line = line + '  '

  #add the stars to the end of the line
    while(j<i):  
      j = j + 1
      line = line + '*'
	
	
  #print the 20-i'th line	
    print(line)	
    i= i - 1
  
#print the last line
  print('     *************************')

#print blank lines as specified

  print(' ')
  print(' ')

main()