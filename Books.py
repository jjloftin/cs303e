#  File: Books.py

#  Description: Assignment 10. Create a program that compares the vocabulary of two authors using two input texts of each author.

#  Student Name: Johnathon Lotin

#  Student UT EID: jjl2328

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: August 13th, 2014

#  Date Last Modified: August 13th, 2014


word_dict = {}
def create_word_dict():
  inWords = open('words.txt', 'r')
  for line in inWords:
    word_dict[line.strip()] = 1
    
  inWords.close()

#remove the punctuation marks from a string [except apostrophes unless it is at the ends of line or in an instances of " 's " at the end of lines]
def parse_string(s):
  

  #start empty string, iterate through old string and add characters
  s_prime = ''
  
  for i in range(len(s)):
    #add letters and spaces
    if(s[i].isalpha() or s[i].isspace()):
      s_prime += s[i]
    #if character is an apostrophe not followed by an s, add it
    elif(s[i] == '\'' and s[i+1] != '\'s' ):
      s_prime += s[i]
    #otherwise just add space
    else:
      s_prime += ' '

  return  s_prime

  #takes input file and returns a dictionary with words in the file as keys with their frequencies for pair values
def get_word_freq(file):
  #create empty dictionary for frequency dictionary
  freq_dict = {}
  #open book
  inFile = open(file, 'r')
  
  #read in each line of the text, parse it for punctuation, then split the line into a list and read each word into the dictionary
  for line in inFile:
    line = line.rstrip()
    line = line.replace('-', ' ')
    if(line.endswith('\'')):
      line = line[:len(line) - 1]
    elif(line.endswith('\'s')):
      line = line[:len(line) - 2]
      
    for word in (parse_string(line)).split():
      if word in freq_dict:
        freq_dict[word] += 1
      else:
        freq_dict[word] = 1
        
  #close book
  inFile.close()
        
  #check each key in the dictionary, if it' capitalized, add it to the list cap_words
  cap_words = []
  for key in freq_dict:
    if(key[0].isupper()):
      cap_words.append(key)
    
  #remove all the instances of capitalized words   
  for word in cap_words:
    #if the word is already in the text in lower case form, add those to the lower case entry
    if(word.lower() in freq_dict):
      freq_dict[word.lower()] += freq_dict[word]
    #if instead, the word exists in the word dictionary, then replace the word with it's uncapitalized form
    elif(word.lower() in word_dict):
      freq_dict[word.lower()] = freq_dict[word]
    #delete the capitalized word from the frequency dictionary
    del freq_dict[word]
 
    
  return freq_dict  
  
#count the total words used in a text  
def word_total(freq_dict):
  sum = 0
  for key in freq_dict:
    sum += freq_dict[key]
  return sum  
  
#compares distinct words in two authors works.
def word_comparison(author1, freq1, author2, freq2):
  dist_words1 = len(freq1)
  tot_words1 = word_total(freq1)
  
  #print the individual statistics for each author: distinct words, total words, the percentage of distinct words
  print(author1)
  print('Total distinct words =', dist_words1)
  print('Total words (including duplicates) =', tot_words1)
  print('Ratio (% of total distinct words to total words) =', format(dist_words1 * 100 / tot_words1, '.10f'))
  print()
  
  dist_words2 = len(freq2)
  tot_words2 = word_total(freq2)
  
  print(author2)
  print('Total distinct words =', dist_words2)
  print('Total words (including duplicates) =', tot_words2)
  print('Ratio (% of total distinct words to total words) =', format(dist_words2 * 100 / tot_words2, '.10f'))
  print()
  
  #print the comparative statistics for each author: number of words used by each author that are unique to their texts
  #and their percentage of total use
  
  unique_words1 = 0
  duplicate_unique_words1 = 0
  for word in freq1:
    if(not (word in freq2)):
      unique_words1 += 1
      duplicate_unique_words1 += freq1[word]
  print(author1 + ' used ' + str(unique_words1) + ' words that ' + author2 + ' did not use.')
  print('Relative frequency of words used by ' + author1 + ' not in common with ' + author2 + ' =', format(duplicate_unique_words1 * 100 / tot_words1, '.10f'))
  print()
  
  unique_words2 = 0
  duplicate_unique_words2 = 0
  for word in freq2:
    if(not (word in freq1)):
      unique_words2 += 1
      duplicate_unique_words2 += freq2[word]
  print(author2 + ' used ' + str(unique_words2) + ' words that ' + author1 + ' did not use.')
  print('Relative frequency of words used by ' + author2 + ' not in common with ' + author1 + ' =', format(duplicate_unique_words2 * 100 / tot_words2, '.10f'))
  
def main():
  #populate word_dict
  create_word_dict()
  
  
  #Enter file name of two books
  book1 = input('Enter the name of the first book: ')
  book2 = input('Enter the name of the second book: ')
  print()
  
  #Enter the respective names of the authors
  author1 = input('Enter the last name of the first author: ')
  author2 = input('Enter the last name of the second author: ')
  print()
  
  #get frequency dictionary of the two books
  freq1 = get_word_freq(book1)
  freq2 = get_word_freq(book2)

  #compare the individual and comparison statistics of the two authors texts. Print the results
  word_comparison(author1, freq1, author2, freq2)

main()