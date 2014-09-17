#  File: Hailstone.py

#  Description: Assignment 4. For a given range of positive values compute the largest number with the largest hailstone sequence. 

#  Student Name: Johnathon Loftin 

#  Student UT EID: jjl2328

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: July 8th, 2014

#  Date Last Modified: July 8th, 2014


def main():
  
  #prompt user for smallest number in the range
  range_low = eval(input('Enter starting number of the range: '))
  range_high = eval(input('Enter ending number of the range: '))
  
  #check to make sure the range is positive
  while(range_low <= 0):
    range_low = eval(input('Enter starting number of the range (must be larger than 0): '))
  while(range_high <= 0):
    range_low = eval(inout('Enter the ending number of the range (must be larger than 0): '))
  
  #check to make sure range_low < range_high
  while( range_low >= range_high ):
    range_low = eval(input('Enter the starting number of the range: '))
    range_high = eval(input('Enter the ending number of the range: '))
  

  
  #initialize variable to store the longest sequence
  max_seq = 0
    
  #initialize variable to store the largest number that produces the largest sequence
  max_num = 1
  
  #find the largest number with the longest hailstone sequence  
  for n in range(range_low, range_high + 1):
    
    #iterator to count the length
    i = 0
    #store original value for n
    n_orig = n
    #run the hailstone sequence
    while(n != 1):
      if( n % 2 == 0):
        n = n // 2
      else:
        n = 3 * n + 1
      i = i + 1
    
    #check if sequence is equal in length to max_seq
    if (i >= max_seq):  
      max_num = n_orig
      max_seq = i

  print('The number ' + str(max_num) + ' has the longest cycle length of ' + str(max_seq) + '.')
  
main()