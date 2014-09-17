#  File: WordSearch.py

#  Description: Assignment 9. Go through a 2D array of characters and find a given list of words

#  Student Name: Johnathon Loftin

#  Student UT EID: jjl2328

#  Course Name: CS 303E 

#  Unique Number: 90110

#  Date Created: August 4, 2014

#  Date Last Modified: August 4, 2014


def main():
  
  #read in the input file
  hiddenText = open('hidden.txt', 'r')
  
  #open output file
  foundText = open('found.txt', 'w')
  
  #input the number of rows and columns in the word search (number of rows index = 0, number of columns index = 1)
  numRowsAndCols = hiddenText.readline().split()
  hiddenText.readline()
  
  #convert strings to numbers
  for i in range(len(numRowsAndCols)):
    numRowsAndCols[i] = eval(numRowsAndCols[i])
  
  #read in the word search
  wordSearch = []
  for i in range(numRowsAndCols[0]):
    wordSearch.append(hiddenText.readline().split())
  hiddenText.readline()
  
  #read in number of words to find
  numWords = eval(hiddenText.readline())
  
  #read in the list of words to find in the word search
  wordList = []
  for i in range(numWords):
    wordList.append((hiddenText.readline().strip()))
  
  #find longest word in the wordlist (we use this for formatting output)  
  if(len(wordList) >= 1):
    formattingCharacters = len(max(wordList, key = len))
  
  #do the word search, store the output indexes in a list
  wordIndex = []  
  for k in range(len(wordList)):
    wordIndex.append([0,0])
    
    #search the word search horizontally for words. Write location to output file
    for i in range(numRowsAndCols[0]):
      s = ''
      for j in range(numRowsAndCols[1]):
        s += wordSearch[i][j]
      if(s.find(wordList[k]) > -1):
        wordIndex[k] = [i + 1, s.find(wordList[k]) + 1]
      elif(s.find(wordList[k][::-1]) > -1):
        wordIndex[k] = [i + 1, s.find(wordList[k][::-1]) + len(wordList[k])]

        
    #search the word search vertically for words.
    for j in range(numRowsAndCols[1]):
      s = ''
      for i in range(numRowsAndCols[0]):
        s+= wordSearch[i][j]
      if(s.find(wordList[k]) > -1):
        wordIndex[k] = [(s.find(wordList[k])) + 1, j + 1]
      elif(s.find(wordList[k][::-1]) > -1):
        wordIndex[k] = [s.find(wordList[k][::-1]) + len(wordList[k]), j + 1]
    ####EXTRA CREDIT#####
    #search the word search diagonally for words number of diagonals going up from left to right is equal to 2 * (numRows + numCols - 1)
    for z in range(numRowsAndCols[1] + numRowsAndCols[0] - 1):
      s = ''
      #search diagnols going up from left to right
      
      #if we're parsing through the upper left half (i + j <= numRows), use this loop
      if(z <= (numRowsAndCols[0] - 1)):
        i = z
        j = 0       
        while(i >= 0 and j < numRowsAndCols[1]):
          s += wordSearch[i][j]
          i -= 1
          j += 1
        if(s.find(wordList[k]) > -1):
          wordIndex[k] = [(z+1) - s.find(wordList[k]), s.find(wordList[k]) + 1]
        elif(s[::-1].find(wordList[k]) > -1):
          wordIndex[k] = [s[::-1].find(wordList[k]) + 1 ,(z+1) - s[::-1].find(wordList[k])]
      
      #if we're parsing through the bottom right half (i + j > numRows), use this loop      
      if(z > (numRowsAndCols[0] - 1)):
        i = numRowsAndCols[0] - 1
        j = (z - numRowsAndCols[0]) + 1
        while(j < numRowsAndCols[1]):
          s += wordSearch[i][j]
          i -= 1
          j += 1
        if(s.find(wordList[k]) > -1):
          wordIndex[k] = [numRowsAndCols[0] - s.find(wordList[k]), (z+1) - numRowsAndCols[0] + s.find(wordList[k]) + 1]
        elif(s[::-1].find(wordList[k]) > -1):
          wordIndex[k] = [(z+1) - numRowsAndCols[0] + s[::-1].find(wordList[k]) + 1, numRowsAndCols[0] - s[::-1].find(wordList[k])]
        
               
      #if have found the word diagonally alredy break from the loop
      if(wordIndex[k][0] > 0 and wordIndex[k][0] > 1):
        break
        
      #now search diagnols going up from right to left (starting at index (numRows - 1, 0))
      s = ''
      if(z <= (numRowsAndCols[0] - 1)):
        i = z
        j = numRowsAndCols[1] - 1
        while(i >= 0): 
          s += wordSearch[i][j]
          i -= 1
          j -= 1
        if(s.find(wordList[k]) > -1):
          wordIndex[k] = [(z+1) - s.find(wordList[k]), numRowsAndCols[1] - s.find(wordList[k])]
        elif(s[::-1].find(wordList[k]) > -1):
          wordIndex[k] = [(z+1) - s.find(wordList[k][::-1]) - (len(wordList[k])-1), numRowsAndCols[1] - s.find(wordList[k][::-1]) - (len(wordList[k])-1) ]
      
        
      if(z > (numRowsAndCols[0] - 1)):
        i = numRowsAndCols[0] - 1
        j = -z  + numRowsAndCols[0] + numRowsAndCols[1] - 2
        
        while(j >= 0):
          s += wordSearch[i][j]
          i -= 1
          j -= 1
        if(s.find(wordList[k]) > -1):
          wordIndex[k] = [numRowsAndCols[0] - s.find(wordList[k]), (-z + numRowsAndCols[0] + numRowsAndCols[1] - 2) - s.find(wordList[k]) + 1 ]
        elif(s[::-1].find(wordList[k]) > - 1):
          wordIndex[k][0] = (numRowsAndCols[0] - s.find(wordList[k][::-1])) - (len(wordList[k]) - 1)
          wordIndex[k][1] = ((-z + numRowsAndCols[0] + numRowsAndCols[1] - 2) - s.find(wordList[k][::-1]) + 1) - s.find(wordList[k][::-1]) - (len(wordList[k]) - 1)
        
    
        ###END EXTRA CREDIT###
  
  #write results to output file  
  for i in range(len(wordList)):
    foundText.write(wordList[i] + ' ' * (formattingCharacters - len(wordList[i])))
    for item in wordIndex[i]:
      foundText.write(format(item, '3d') + ' ')
    foundText.write('\n')
  
  #close input/output files
  hiddenText.close()
  foundText.close()
        
main()