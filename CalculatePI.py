#  File: CalculatePI.py

#  Description: Assignment 6. Use random number generation to estimate PI. As input, take a number of uniformly distributed throws on a  square dartboard of 
#  side length 2 with a circle of radius 1 inscribed within. The area of the circle = Pi, The area of the square = 4. Since the throws are uniformly
#  distributed, the ratio of the number of throws hitting the circle vs hitting outside the circle should approach pi/4 as number of throws grows without
#  bound.

#  Student Name: Johnathon Loftin 

#  Student UT EID: jjl2328

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: July 21st, 2014

#  Date Last Modified: July 21st, 2014

import math
import random

#estimate pi by using random number generation using the algorithm as in the description.
def ComputePI (numThrows):
  numHits = 0
  
  iterator = 1
  while(iterator <= numThrows):
    xPos = random.uniform(-1.0, 1.0)
    yPos = random.uniform(-1.0, 1.0)

    if(math.hypot(xPos,yPos) < 1):
      numHits += 1
    
    iterator += 1
    
  PI = 4 * (numHits / numThrows)  

  return PI  

 
#produce a table of values showing how accuracy of estimation scales with increased number of randomly generated numbers
def main():

  i = 0
  
  while(i < 6):
    
    num = 100 * (10 ** i)
    PI = ComputePI (num)
    Difference = PI - math.pi
    
    print('num = ' + format(num, '<8'), end = '   ')
    print('Calculated PI = ' + format(PI, '.6f'), end = '   ')
    
    if(Difference > 0):
      print('Difference = +' + format(Difference, '.6f'))
     
    else:
      print('Difference = ' + format(Difference, '.6f'))
    
    i += 1

main()