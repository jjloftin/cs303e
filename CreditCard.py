#  File: CreditCard.py

#  Description: Assignment 5. Write a program that determines whether or not it's valid and if it is valid if it is a MasterCard, Discover, Visa, 
#  or American Express credit card 

#  Student Name: Johnathn Loftin 

#  Student UT EID: jjl2328

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: July 18th, 2014

#  Date Last Modified: July 18th, 2014

#define a function to check the number of digits. Returns true if input is 15 or 16 digits long.
def DigitChecker(cc_num):

  if((len(str(cc_num)) == 15) or (len(str(cc_num)) == 16)):
    return True
  else:
    return False

#assuming input has valid number of digits, apply Luhn's test to the number and check its validity.
def is_valid(cc_num):

  cc_digits = []
  len_num = len(str(cc_num))
  for i in range (len_num):
    cc_digits.append(cc_num % 10)
    cc_num = cc_num // 10

  #double the odd digits and then take the sum of the digits of the odd digits
  for i in range (1, len_num, 2):
    cc_digits[i] = (cc_digits[i] * 2) % 10 + (cc_digits[i] * 2) // 10
  
  sum_all_digits = 0
  
  for i in range(len_num):
    sum_all_digits += cc_digits[i]

  if (sum_all_digits % 10 == 0):
    return True
  else:
    return False
    
    
    

#determine and return the credit card type.
def cc_type(cc_num):
  
  cc_digits = []
  len_num = len(str(cc_num))
  
  for i in range (len_num):
    cc_digits.append(cc_num % 10)
    cc_num = cc_num // 10
  
  #flip the digits so they read left to right as entered by user
  for i in range (len_num // 2):
    cc_digits[i], cc_digits[len_num - 1 - i] = cc_digits[len_num - 1 - i], cc_digits[i]
    
  
  #print(cc_digits)
  
  if (cc_digits[0] == 3 and ((cc_digits[1] == 4) or (cc_digits[1] == 7))):
    return 'American Express '
  
  elif (cc_digits[0] == 6):
    if((cc_digits[1] == 0) and (cc_digits[2] == 1) and (cc_digits[3] == 1)):
      return 'Discover '
    elif((cc_digits[1] == cc_digits[2]) and (cc_digits[1] == 4)):
      return 'Discover '
    elif((cc_digits[1] == 5)):
      return 'Discover '

  elif(cc_digits[0] == 5 and cc_digits[1] <= 5):
    return 'MasterCard '
  
  elif(cc_digits[0] == 4):
    return 'Visa '
  
  else:
    return ''
   
#prompt user to enter a credit card number and check it for validity and type of card
def main():

  cc_num = int(input('Enter a 15 or 16 digit number: '))
  
  #check number of digits
  if(not DigitChecker(cc_num)):
    print('Not a 15 or 16-digit number.')
    return ''
  
  if(is_valid(cc_num)):
    print('Valid ' + cc_type(cc_num) + 'credit card number')
  else:
    print('Invalid credit card number')


main()





