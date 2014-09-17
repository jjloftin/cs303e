#  File: EasterSunday.py

#  Description: Assignment 2. Given a year, this program computes the date of Easter Sunday

#  Student Name: Johnathon Loftin

#  Student UT EID: jjl2328

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: Tuesday, June 24th 2014

#  Date Last Modified: Tuesday, June 25th 2014

############################################################################

def main():
  #Get year
  y = eval (input ('Enter year: '))
   

  #Given year, use Gaussian algorithm to compute date of Easter Sunday
  
  a = y % 19
  b = y // 100
  c = y % 100
  
  d = b // 4
  e = b % 4
  
  g = (8 * b + 13) // 25
  
  h = (19 * a + b - d - g + 15) % 30
  #print(h)
  
  j = c // 4
  k = c % 4
  
  m = (a  + 11 * h) // 319
  #print(m)
  
  r = (2 * e + 2 * j - k - h + m + 32) % 7
  #print(r)
  
  n = (h - m + r + 90) // 25
  
  p = (h - m + r + n + 19) % 32
  
  # Write out the date for Easter Sunday
  if (n == 3):
    print ('In', y, 'Easter Sunday is on', p, 'March.')
  else:
    print ('In', y, 'Easter Sunday is on', p, 'April.')

	 
main()