#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""                                               
850b9ded5b06a25e0cd76b6b8db48cba generated for miis15 at 2015-02-11 14:11:26 
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 1 - python 
 
If you need to peek at examples or just want to know more, take a look at
the page: https://docs.python.org/3/library/index.html. Here you will find
everything this lab will go through and much more. 
"""

"""
--------------------------------------------------------------------------
Section 1. Integers, strings, floats and basic arithmetics 
 
The foundation of numbers and basic arithmetic. 
"""

"""
Exercise 1.1 
 
Create a variable called 'numOne' and give it the value 56. Create another
variable called 'numTwo' and give it the value 33. Create a third variable
called 'result' and assign to it the sum of the first two variables. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
numOne = 56
numTwo = 33
ANSWER = numOne + numTwo

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Create a variable called 'numThree' and give it the value 17. Create
another variable called 'numFour' and give it the value 18. Subtract
'numThree' from 'numFour' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
numThree = 17
numFour = 18
ANSWER = numFour - numThree

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Find out the product of 'numOne' and 'numThree' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = numOne * numThree

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Divide 30 with 5 and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = 30 / 5

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Create a variable called 'floatOne' and give it the value 33.3. Create
another variable called 'floatTwo' and give it the value 92.08. Sum the two
values and answer with the result, rounded to 2 decimals. 

Write your code below and put the answer into the variable ANSWER.
"""
floatOne = 33.3
floatTwo = 92.08
ANSWER = round(floatOne + floatTwo, 2)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Subtract 'floatTwo' from 'floatOne' and answer with the result. Round to 2
decimals. 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = round(floatOne - floatTwo, 2)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Answer with the product of 'floatOne' and 'floatTwo', rounded to 4
decimals. 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = round(floatOne * floatTwo, 4)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Create three variables: 'n1' = 386, 'n2' = 302 and 'n3' = 68. Sum up 'n1'
and 'n2'. Subtract 'n3' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
n1 = 386
n2 = 302
n3 = 68
ANSWER = n1 + n2 - n3

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Answer with the result of 443 modulo (%) 21. 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = 443 % 21

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10 
 
Add the word: 'storage' to the word: 'icecream' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = 'icecream' + 'storage' 

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Conditions, exceptions, booleans, if, else and elif 
 
 
"""

"""
Exercise 2.1 
 
Answer with the boolean value of: 124 is less than 33. 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = bool(123 < 33)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Answer with the boolean value of: 430 is larger than 254. 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = bool(430 > 254)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Answer with the boolean value of: 124 == 430. 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = bool(124 == 430)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Create three variables representing dice values: 'd1' = 2, 'd2' = 6 and
'd3' = 2. Sum them up and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
d1 = 2
d2 = 6
d3 = 2
dlist = [d1, d2, d3]
ANSWER = sum(dlist)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Create an if statement to see if the total value of your dices is 11 or
higher. If that is the case, answer with the string: 'big', else answer
with the string: 'nothing'.  

Write your code below and put the answer into the variable ANSWER.
"""
totalDiceValue = 3
if totalDiceValue >= 11:
    ANSWER = 'big'
else:
    ANSWER = 'nothing'

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6 
 
Create an elif statement that checks your total dice value. The checks and
results should be: three of the same value = 'triple', total of 11 or
higher = 'big', total of 10 or lower = 'small'. If you get a triple you
should not make more checks. 

Write your code below and put the answer into the variable ANSWER.
"""
diceValue1 = 2
diceValue2 = 6
diceValue3 = 2
if diceValue1 == diceValue2 == diceValue3:
    result = 'triple'
elif diceValue1 + diceValue2 + diceValue3 >= 11:
    result = 'big'
elif diceValue1 + diceValue2 + diceValue3 <= 10:
    result = 'small'
ANSWER = result
# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Built-in functions 
 
Some useful built-in functions 
"""

"""
Exercise 3.1 
 
Use max() to find the largest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = max(6, 8, 95, 2, 12, 152, 4, 78, 621, 45)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2 
 
Use min() to find the smallest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = min(6, 8, 95, 2, 12, 152, 4, 78, 621, 45)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))

"""
Exercise 3.3 
 
Use len() to find the number of letters in the word: memory. Answer with
the result. 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = len('memory')

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.3", ANSWER, False))

"""
Exercise 3.4 
 
Convert the number 65 to a string and add it to the word 'memory'. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
ANSWER = 'memory' + str(65)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.4", ANSWER, False))

"""
Exercise 3.5 
 
Convert the number 677.31 to an integer and then to a string. Add it to the
beginning of the word: 'memory'. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
text = int(677.31)
text = str(text)
ANSWER = text + 'memory'

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.5", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 4. Functions 
 
Basic functions 
"""

"""
Exercise 4.1 
 
Create a function called 'prodNr' that takes two arguments, 31 and 65. The
function should return the product of the numbers. Answer with a call to
the function.  

Write your code below and put the answer into the variable ANSWER.
"""
def prodNr(a, b):
    """Multiply two numbers"""
    return a * b
ANSWER = prodNr(31, 65)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.1", ANSWER, False))

"""
Exercise 4.2 
 
Create a function called 'funnyWord' that takes one argument and adds it to
the string ' is a funny word'. If the argument is 'water', the function
should return: 'water is a funny word'. Use the argument 'resort' and
answer with a call to the function. 

Write your code below and put the answer into the variable ANSWER.
"""
def funnyWord(a):
    """Add argument to string"""
    return a + ' is a funny word'
ANSWER = funnyWord('resort')

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.2", ANSWER, False))

"""
Exercise 4.3 
 
Create a function called 'inRange' that takes one argument. The function
should return 'true' if the argument is higher than 50 and lower than 100.
If the number is out of range, the function should return 'false'. The
return type should be boolean. Use the argument 18 and answer with a call
to the function. 

Write your code below and put the answer into the variable ANSWER.
"""
def inRange(a):
    """Check if a number is in or out of range"""
    if 50 < a < 100:
        return True
    else:
        return False
ANSWER = inRange(18)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.3", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 5. Iteration and loops 
 
For-loops and while-loops.  
"""

"""
Exercise 5.1 
 
Create a while-loop that adds 3 to the number 46, 40 times. Answer with the
result.  

Write your code below and put the answer into the variable ANSWER.
"""
count = 0
Number = 46
while count < 40:
    Number = Number + 3
    count = count + 1
ANSWER = Number

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.1", ANSWER, False))

"""
Exercise 5.2 
 
Create a while-loop that subtracts 9 from 40, 71 times. Answer with the
result.  

Write your code below and put the answer into the variable ANSWER.
"""
count = 0
Number = 40
while count < 71:
    Number = Number - 9
    count = count + 1
ANSWER = Number

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.2", ANSWER, False))

"""
Exercise 5.3 
 
Create a for-loop that counts the number of elements in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
count = 0
for itervar in [6, 8, 95, 2, 12, 152, 4, 78, 621, 45]:
    count = count + 1
ANSWER = count

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.3", ANSWER, False))

"""
Exercise 5.4 
 
Create a for-loop that sums up the numbers in the serie:
67,2,12,28,128,15,90,4,579,450. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
theSum = 0
for i in [67, 2, 12, 28, 128, 15, 90, 4, 579, 450]:
    theSum = theSum + i
ANSWER = theSum

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.4", ANSWER, False))

""" Another way for 5.4
def sum(x, y):
	return x+y
theSum = reduce(sum, [67,2,12,28,128,15,90,4,579,450], 0);
ANSWER = theSum
"""

"""
Exercise 5.5 
 
Create a for-loop that finds the largest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
nums = [6, 8, 95, 2, 12, 152, 4, 78, 621, 45]
maxValue = min(nums)
for n in nums:
    if n >= maxValue: 
        maxValue = n

ANSWER = maxValue

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.5", ANSWER, False))

"""
Exercise 5.6 
 
Create a for-loop that goes through the numbers:
67,2,12,28,128,15,90,4,579,450. If the current number is even, you should
add it to a variable and if the current number is odd, you should subtract
it from the variable. Answer with the final result.  

Write your code below and put the answer into the variable ANSWER.
"""
nums = [67, 2, 12, 28, 128, 15, 90, 4, 579, 450]
value = 0
for n in nums:
    if n % 2 == 0:
        value = value + n
    else:
        value = value - n
ANSWER = value

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.6", ANSWER, False))

dbwebb.exitWithSummary()
