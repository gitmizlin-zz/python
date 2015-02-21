#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""                                               
4603064a1dbd86df0e96e21868f97217 generated for miis15 at 2015-02-21 08:21:09 
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 2 - python 
 
Strings and files 
"""

"""
--------------------------------------------------------------------------
Section 1. Strings 
 
The basics of strings 
"""

"""
Exercise 1.1 
 
Assign the word: 'lollipop' to a variable and put your variable as the
answer. 

Write your code below and put the answer into the variable ANSWER.
"""

text = "lollipop"
ANSWER = text


# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Assign the word 'lollipop' to a variable. Create another variable where you
put the first and the last letter in the word. Answer with the second
variable. 

Write your code below and put the answer into the variable ANSWER.
"""

text = "lollipop"
firstLetter = text[:1] 
lastLetter = text[-1:]

ANSWER = firstLetter + ", " + lastLetter

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Assign the word: banana to a variable. Answer with the length of the word
as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
text = "banana"
lengthOfText = len(text)

ANSWER = lengthOfText

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Use the 'in-operator' to see if the word: 'melon' contains the letter 'a'.
Answer with a boolean result. 

Write your code below and put the answer into the variable ANSWER.
"""
word = "melon"
result = 'a' in word

ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Make all the letters in the word 'banana' capitalized. Answer with the
capitalized word. 

Write your code below and put the answer into the variable ANSWER.
"""
text = "banana"
textCapital = text.upper()

ANSWER = textCapital

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Use the built-in function 'startswith()' to see if the word 'orange' starts
with the letter 'n'. Answer with the boolean value. 

Write your code below and put the answer into the variable ANSWER.
"""
word = "orange"
result = word.startswith("n")

ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Assign the words: 'car' and 'apple' to two different variables. Create a
function and pass the two words as arguments to it. Your function should
return them as a single word. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
word1 = "car"
word2 = "apple"

def conWords(var1, var2):
	return(var1 + var2)

ANSWER = conWords(word1, word2)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Create a function and pass the word: 'lollipop' to it. Your function should
return the sentence: 'This word was: lollipop'. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
word = "lollipop"

def makeSentence(var):
	return("This word was: " + var)

ANSWER = makeSentence(word)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Create a function and pass the word: 'apple' to it. Your function should
return the string 'yes' if the word is longer than 5 characters. Else
return 'no'. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
word = "apple"

def checkLen(var):
	if len(var) > 5:
		return "yes"
	else:
		return "no"

ANSWER = checkLen(word)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10 
 
Create a function and pass the word: 'banana' to it. Your function should
return a string with the word backwards. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
word = "banana"

def backwards(var):
	return var[::-1]

ANSWER = backwards(word)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
Exercise 1.11 
 
Create a function and pass the word: 'car' to it. Your function should
exclude the first and the last letter of the word and return it. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
def excludeFirstAndLastLetter(var):
	return str.strip(var[1:-1])

ANSWER = excludeFirstAndLastLetter("car")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
Exercise 1.12 
 
Use the format operator to print out: 'My 'string' has 'integer' 'string''.
Use the values: 'grandma', '42' and 'cows'. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

def formatOperator(string1, integer, string2):
    return "My %s has %s %s." % (string1, integer, string2)

ANSWER = formatOperator("grandma", 42, "cows")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.12", ANSWER, False))

"""
Exercise 1.13 
 
Use 'find' and 'slice' on the string: '984.45.6.65 : (wasp), boat' to get
the word inside the parenthesis. Answer with the word as a string. 

Write your code below and put the answer into the variable ANSWER.
"""

text = "984.45.6.65 : (wasp), boat"
parenthesis1 = "("
sliceIndex1 = text.index("(")	
sliceIndex2 = text.index(")")	
ANSWER = text[sliceIndex1+1:sliceIndex2]

# def findAndSlice(var):
# 	parenthesis1.find(text)
# 	parenthesis1.find(text)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Files 
 
This section uses the text file: 'httpd-access.txt' 
"""

"""
Exercise 2.1 
 
Open the file and count the number of times a line starts with '81'. Answer
with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Find out the last 4 digits on line 821 in the file. Answer with the result
as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Find out which of the ip adresses 81.226.253.26 and 95.19.133.73 that has
the highest amount of entries. Answer with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Count the number of periods (.) there are in the file. Use the built-in
function count() on the file after you have converted it to a string.
Answer with the result as an integer.  

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Find the characters on line 637 from index 65 to index 75. Make sure that
the character at index 75 also gets included. Answer with the piece of
string you found. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6 
 
Find the last element on each line and sum all that are even numbers.
Answer with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))


dbwebb.exitWithSummary()
