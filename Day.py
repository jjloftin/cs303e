#  File: Day.py

#  Description: Assignment 3. Given a date with day/month/year between 1900 and 2100, calculate the day of the week of the date

#  Student Name: Johnathon Loftin

#  Student UT EID: jjl2328

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: July 3rd, 2014

#  Date Last Modified: July 4th, 2014

##################################################

def main():
  
  #prompt user to enter year
  year = eval( input( 'Enter year: '))

  #check the year and then correct the year if necessary
  while ((year < 1900) or (year > 2100)):
    year = eval( input( 'Enter year (between 1900 and 2100): '))

  #prompt user to enther month
  month = eval( input( 'Enter month: '))

  #check the month. correct if necessary
  while ( (month < 0) or (month > 12) ):
    month = eval(input( 'Enter month (Jan = 1, Feb = 2, etc): '))

  #prompt user to enter the day
  day = eval( input( 'Enter day: '))

  #check the day. correct if necessary
  if((month == 1) or (month==3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)):
    while((day > 31) or (day < 0)):
      day = eval(input('Enter day: '))
  
  elif((month == 4) or (month ==6) or (month == 9) or (month == 11)):
    while((day > 30) or (day < 0)):
      day = eval (input('Enter day: '))
  
  #if month is Feburary, check if this year is a leap year
  elif( (month == 2)  and ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0) ))):
    while((day > 29) or (day < 0)):
      day = eval(input('Enter day (Feb. only has 29 days this year): ' ))
  
  else:
    while((day > 28) or (day < 0)):
      if(day == 29):
        day = eval(input('Enter day (This year is not a leap year): '))
      else:
        day = eval(input('Enter day: '))

      
  #create and assign variables as specified for the algorithm
  if (month > 2):
    a = (month - 2)
  else:
    a = month + 10
  
  b = day
  d = year // 100
  
  if (month > 2):
    c = year - d * 100 
  else:
    c = year - d * 100 - 1 

  #print(a, b, c, d)
  
  #run the algorithm to calculate the day of the week
  w = (13 * a - 1) // 5
  x = c // 4
  y = d // 4
  z = w + x + y + b + c - 2 * d
  r = z % 7
  r = (r + 7) % 7
 #initiate part of the print statement to type less
  s = 'The day is '
  
 
  #print the day of the date as calculated by the algorithm
  if (r == 1):
    print(s + 'Monday')
  elif (r == 2):
    print(s + 'Tuesday')
  elif(r == 3):
    print(s + 'Wednesday')
  elif(r == 4):  
    print(s + 'Thursday')
  elif(r == 5):
    print(s + 'Friday')
  elif(r == 6):
    print(s + 'Saturday')
  elif(r == 0):
    print(s + 'Sunday')
	
main()