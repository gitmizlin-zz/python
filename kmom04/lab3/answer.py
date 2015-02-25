#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""                                               
d40115428ebee24e59a1998c8b6120d5 generated for miis15 at 2015-02-25 11:49:34 
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 3 - python 
 
 
"""

"""
--------------------------------------------------------------------------
Section 1. List basics 
 
 
"""

"""
Exercise 1.1 
 
Concatenate the two lists [ozelot, Berenger] and [lion, desk]. Answer with your list.  
Write your code below and put the answer into the variable ANSWER.
"""
def listConcatenetion (list1, list2):
    """
    Concatenate two lists.
    """
	return list1 + list2

a = ["ozelot", "Berenger"]
b = ["lion", "desk"]

ANSWER = listConcatenetion(a, b)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Use the list [Dafoe, Sheen, Berenger, Depp, Whitaker]. Add the words:
'purple' and 'pirate' as the second and third element. Answer with the
modified list. 

Write your code below and put the answer into the variable ANSWER.
"""

def addToList(listName, word1, index1, word2, index2):
	"""
	Add two elements to a list.
	"""

	listName.insert(index1, word1)
	listName.insert(index2, word2)
	return listName

myList = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]

ANSWER = addToList(myList, "purple", 1, "pirate", 2)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Use the list [Dafoe, Sheen, Berenger, Depp, Whitaker]. Replace the third
word with: 'potato'. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""

def replaceList(listName, index, word):
	"""
	Replace an element in a list by index.
	"""
    listName[index-1] = str(word)

    return listName

myList = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]

ANSWER = replaceList(myList, 3, "potato")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Sort the list [wasp, fly, butterfly, bumblebee, mosquito] in ascending
alphabetical order. Answer with the sorted list. 

Write your code below and put the answer into the variable ANSWER.
"""

def sortListAlphabetAsc(listName):
    """
    Sort the elements in a list in ascending alphabetical order.
    """
    return sorted(listName)

myList = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]

ANSWER = sortListAlphabetAsc(myList)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Use the list from the last excercise ([wasp, fly, butterfly, bumblebee,
mosquito]) and sort it in decending alphabetical order. Answer with the
sorted list. 

Write your code below and put the answer into the variable ANSWER.
"""
def sortListAlphabetDec(listName):
    """
    Sort the elements in a list in decending alphabetical order.
    """
    return sorted(listName, reverse=True)

myList = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]

ANSWER = sortListAlphabetDec(myList) 

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Use pop() to get the second and the last element in the list: [Dafoe,
Sheen, Berenger, Depp, Whitaker]. Answer with the popped elements in a new
list. 

Write your code below and put the answer into the variable ANSWER.
"""

def getElementsFromList(listName):
    """
    Get second and the last element from a list by index in a new list.
    """
    
    newList = [listName.pop(1), listName.pop()]
    return newList
    
myList = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]

ANSWER = getElementsFromList(myList)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Use remove() to delete the word: 'bumblebee' from the list: [wasp, fly,
butterfly, bumblebee, mosquito]. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
def deleteElementFromList(listName, elementToDelete):
	"""
	Delete an element from a list.
	"""
	listName.remove(elementToDelete)
	return listName

myList = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]

ANSWER = deleteElementFromList(myList, "bumblebee")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Built-in list functions 
 
Some basic built-in functions 
"""

"""
Exercise 2.1 
 
Use a built-in function to sum all numbers in the list: [567, 23, 12, 36,
7]. Answer with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
def getSumfromList(listName):
    """
    Get the sum of all numbers in a list.
    """
    sum = 0
    for number in listName:
        sum = sum + number

    return sum

myList = [567, 23, 12, 36, 7]

ANSWER = getSumfromList(myList)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Use built-in functions, such as 'sum' and 'len' to get the average value of
the list: [45, 22, 2, 498, 78]. Answer with the result as a float with at
most one decimal. 

Write your code below and put the answer into the variable ANSWER.
"""
def getAverageFromList(listName):

    total = sum(listName)
    return "{0:.2f}".format(total/len(listName))

myList = [45, 22, 2, 498, 78]

ANSWER = getAverageFromList(myList)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Use a built-in function to get the lowest number in the list: [45, 22, 2,
498, 78]. Answer with the result as a integer. 

Write your code below and put the answer into the variable ANSWER.
"""
def getLowestFromList(listName):
    """
    Get the lowest number in the list.
    """
    return min(listName)

myList = [45, 22, 2, 498, 78] 

ANSWER = getLowestFromList(myList)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Use the built-in functions split() and join() to fix this string:
'The?wind?is?blowing' into a real sentence, (without '?'). Answer with the
fixed string. 

Write your code below and put the answer into the variable ANSWER.
"""
def splitAndJoin(sentence):
    """
    Split a string and join words with a space between.
    """
    
    words = sentence.split("?")
    return " ".join(words)

ANSWER = splitAndJoin("The?wind?is?blowing")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Use the string: 'Whenever I feel the need to exercise, I lie down until it
goes away.' and split it with the delimiter ' ' (space). Answer with the
element at index 10. 

Write your code below and put the answer into the variable ANSWER.
"""
def splitAndGetElement(sentence):
    """
    Split a string with space and return the element at index 10.
    """

    words = sentence.split(" ")
    return words[10]

mySentence = "Whenever I feel the need to exercise, I lie down until it goes away."

ANSWER = splitAndGetElement(mySentence)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6 
 
Use slice on the list [dvd, mp3, blu-ray, vhs, cd] and replace the second
and third element with 'green, purple'. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
def replaceElements(listName, var):
    """
    Replace elements in a list
    """
    listName[1:2] =  var
    return listName

myList = ["dvd", "mp3", "blu-ray", "vhs", "cd"]
myVar = "green, purple"

ANSWER = replaceElements(myList, myVar)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
Exercise 2.7 
 
Use slice on the list [dvd, mp3, blu-ray, vhs, cd] and replace the last two
elements with 'green, purple'. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.7", ANSWER, False))

"""
Exercise 2.8 
 
Use slice on the list [dvd, mp3, blu-ray, vhs, cd] and insert the words
'green, purple' after the third element. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.8", ANSWER, False))

"""
Exercise 2.9 
 
Use 'del' on the list [tree, stone, grass, water, sky] and delete the first
element. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.9", ANSWER, False))

"""
Exercise 2.10 
 
Use 'del' on the list [tree, stone, grass, water, sky] and delete the
second and third element. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.10", ANSWER, False))

"""
Exercise 2.11 
 
Assign the list [a, b, c, d, e] to a variable called 'list1'. Assign the
list again, but to another variable called 'list2'. Answer with the result
of 'list1 is list2'.  

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.11", ANSWER, False))

"""
Exercise 2.12 
 
Use your lists from the last exercise. Assign 'list1' to another variable
called 'list3' like this: list3 = list1. Answer with the result of 'list1
is list3'. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.12", ANSWER, False))

"""
Exercise 2.13 
 
Use your lists from the last exercise. Change the first element in 'list1'
to 'z'. Answer with 'list3'. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Lists as arguments 
 
Some excercises with passing lists as arguments to a function. 
"""

"""
Exercise 3.1 
 
Create a function that returns the list passed as argument sorted in
numerical and ascending order. Also multiply all values with 10. Use the
list: [45, 22, 2, 498, 78], and the built-in method 'sort()'. Answer with
the sorted list. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2 
 
Create a function that takes the list: [45, 22, 2, 498, 78] as argument.
The function should multiply all even numbers by 2 and add 7 to all odd
numbers. Answer with the modified list sorted in numerical order,
descending. 

Write your code below and put the answer into the variable ANSWER.
"""





ANSWER = "Replace this text with the answer or the variable holding it."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))


dbwebb.exitWithSummary()
