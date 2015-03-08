#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mi with a simple menu to start up with.
Mi doesn't do anything, just presents a menu with some choices.
You should add functinoality to Mi.

"""
import math
from random import randint
import random
import datetime
import csv

def menu():
    """
    Display the menu with the options that Mi can do.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(meImage()) 
    print("Välj ett nummer från menyn.\n") 
    print("0) Presentation.") 
    print("1) Ålder till sekunder. Mi ska fråga efter din ålder "
          "och sedan skriva ut hur många sekunder du minst har levt.")
    print("2) Vikt på månen. Mi ska fråga efter en vikt i kg och "
          "sedan skriva ut hur mycket den vikten skulle vara på månen.")
    print("3) Minuter till timmar. Mi ska fråga efter antal minuter "
          "och sedan skriva ut hur många timmar och minuter det motsvarar.")
    print("4) Celcius till Farenheit. Mi ska fråga efter en temperatur "
          "i Celcius och sedan skriva ut motsvarande i Farenheit.")
    print("5) Ordmultiplicering. Mi ska fråga efter ett ord och "
          "en siffra och sedan skriva ut det ordet så många gånger.")
    print("6) Slumpmässiga tal. Mi ska fråga efter min och max "
          "och sedan skriva ut 10 slumpmässiga tal mellan min och max. "
          "Dessa ska skrivas ut kommaseparerat på samma rad.")
    print("7) Summa och medel. Mi ska fråga efter tal tills "
          "du anser dig vara klar (t.ex skriver “done”) och sedan ska "
          "Mi skriva ut summan och medelvärdet för dessa tal.")
    print("8) Poäng till betyg. Mi ska fråga efter maxpoäng samt "
          "dina poäng och sedan ska Mi skriva ut vilket betyg dina poäng motsvarade.")
    print("9) Arean på cirkel. Mi ska fråga efter en radie och räkna ut arean på cirkeln.")
    print("10) Hypotenusan på triangel.Mi ska fråga efter rätvinkliga sidor och räkna ut hypotenusan på triangeln.")
    print("11) Taljämförelse. Mi ska fråga efter tal och för varje tal angivet "
          "så ska Mi skriva ut om det talet var större, mindre eller samma som det förra talet som skrev in.")
    print("12) Guess the number. Mi ska tänka på ett tal mellan 1-100 "
          "och du ska gissa vilket det är. För varje gissning ska Mi "
          "berätta om gissningen var högre eller lägre än det han "
          "tänkte på. Du ska ha 6 gissningar på dig.")
    print("13) Mi ska skriva ut: dagens datum och nuvarande tid, "
          "hur hon mår (slumpmässigt humör), ett heltal, samt ett floattal "
          "med 3 decimaler.")
    print("14) Kasta om bokstäver. Mi ska be dig skriva in ett ord som "
          "sedan slumpmässigt kastas om. Det omkastade ordet ska sedan " 
          "skrivas ut.")
    print("15) Be Mi om ett citat genom att använda hälsningsordeen som 'hej', 'hello', 'hi' m.m."
          "Mi ska presentera ett slumpmässigt citat från boken 'Liftarens Guide till Galaxen'.")
    print("16) Mi har ett inventory där hon kan bära saker. Genom att fråga henne så ska hon kunna: "
          "Visa vad som finns i inventoryt (visa), berätta hur många saker hon bär på (antal), "
          "plocka upp saker du anger (plocka) och kasta bort saker du anger (kasta).")
    print("q) Quit.")

def getInputFromUser(inputText, verifier, error=None):
    """
    General function to get input from the user, repeating the question until verifier returns true
    """
    while True:
        userInput = input(inputText)
        if not verifier or verifier(userInput):
            return userInput
        elif error:
            print(error)

def convertToInt(value):
    """
    General function to convert given data to an int.
    """
    try:
        return int(value)
    except ValueError:
        return False

def presentation():
    """
    Introduce each other. 
    """
    
    inputText = "Hej! Jag heter Mi. Vad heter du?"
    yourName = getInputFromUser(inputText, lambda inputText: inputText)

    print("Tjena", yourName, "!")

def yearToSecond():
    """
    Convert age to seconds.
    """

    ageInYears = getInputFromUser("Hur gammal är du? ", convertToInt, "Du måste mata in en siffra.")

    ageInYears = int(ageInYears)
    ageInSeconds = ageInYears * 31536000
    print("\nDu har levt", ageInSeconds, "sekunder.")    

    # ageInYears = input("Hur gammal är du? ")
    # try:
    #     ageInYears = int(ageInYears)
    #     ageInSeconds = ageInYears * 31536000
    #     print("\nDu har levt", ageInSeconds, "sekunder.")    
    # except:
    #     print("\nDu måste mata in en siffra.")
    #     yearToSecond()

def weightMoon():
    """
    Calculate weight on the moon.
    """

    weight = getInputFromUser("Ange en vikt. ", convertToInt, "Du måste mata in en siffra.")
    
    weight = int(weight)
    weightOnTheMoon = "{0:.2f}".format(weight / 6)
    print("\nVikten på månen är ca", weightOnTheMoon, "kg.") 

    # weight = input("Ange en vikt.  ")
    # try:
    #     weight = int(weight)
    #     weightOnTheMoon = "{0:.2f}".format(weight / 6)
    #     print("\nVikten på månen är ca", weightOnTheMoon, "kg.")  
    # except:
    #     print("\nDu måste mata in en siffra.")
    #     weightMoon()

def minutesToHours():
    """
    Convert minutes to hours.
    """
    minutes = getInputFromUser("Ange en tidslängd i minuter. ", convertToInt, "Du måste mata in en siffra.")
    
    minutes = int(minutes)
    hours = round(minutes / 60)
    minutesModulo = minutes%60 
    print("\nTidslängden är", hours, "timmar och", minutesModulo, "minuter.")  

    # minutes = input("Ange en tidslängd i minuter.  ")
    # try:
    #     minutes = int(minutes)
    #     hours = round(minutes / 60)
    #     minutesModulo = minutes%60 
    #     print("\nTidslängden är", hours, "timmar och", minutesModulo, "minuter.")  
    # except:
    #     print("\nDu måste mata in en siffra.")
    # minutesToHours()

def celciusToFahrenheit():
    """
    Convert celcius to Fahrenheit.
    """

    celcius = getInputFromUser("Ange temperaturen i celcius. ", convertToInt, "Du måste mata in en siffra.")

    celcius = int(celcius)
    fahrenheit = celcius * 9/5 + 32
    print("\nTemperaturen är", fahrenheit, "°F.")  

    # celcius = input("Ange temperaturen i celcius.  ")
    # try:
    #     celcius = int(celcius)
    #     fahrenheit = celcius * 9/5 + 32
    #     print("\nTemperaturen är", fahrenheit, "°F.")  
    # except:
    #     print("\nDu måste mata in en siffra.")
    #     celciusToFahrenheit()

def wordMultiply():
    """
    Repeat a word as many times as given.
    """

    word = getInputFromUser("Ange ett ord: ", lambda inputText: inputText, "Du måste mata in ett ord.")

    angeNumText = "Ange en siffra: "
    varningText = "Du måste ange en siffra."

    numberOfWords = getInputFromUser(angeNumText, convertToInt, varningText)
    numberOfWords = int(numberOfWords)

    for _ in range(numberOfWords):
        print(word)

    # if len(word) != 0:
    #     while True:
    #         numberOfWords = input("Ange hur många gånger du vill skriva ut ordet. ")
    #         try:
    #             numberOfWords = int(numberOfWords)
    #             count = 0
    #             while (count < numberOfWords):
    #                 print (word)
    #                 count = count + 1
    #             break
    #         except:
    #             print("\nDu måste mata in en siffra.") 
    # else:
    #     print("\n")
    #     wordMultiply()

def randomNumbers():
    """
    Return 10 random numbers between given numbers.
    """

    def getNumberFromInput(inputText):
        """
        Get a number from input text.
        """
        while True:
            number = input(inputText)
            try:
                number = int(number)
                return number
            except ValueError:
                print("Du måste mata in ett nummer.")
                
    maxNumber = 0
    minNumber = 0

    while maxNumber <= minNumber: 
        minNumber = getNumberFromInput("Ange ett min-nummer: ")
        maxNumber = getNumberFromInput("Ange ett max-nummer: ")

    # randomNumbersList = []
    # for i in range(10):
    #     randomNumbers.append(randint(minNumber, maxNumber))

    # List comprehension, common in Python
    randomNumbersList = [randint(minNumber, maxNumber) for i1 in range(10)]

    # map = run a function on each element in a list
    print(", ".join(map(str, randomNumbersList)))

    # lamda = anonymous function (function without name) on one line
    # print(", ".join(map(lambda number: str(number), randomNumbersList)))

def sumAndAverage():
    """
    Return the sum and average of given numbers.
    """
    numbers = []

    while True:
        number = getInputFromUser("Mata in en siffra eller 'OK' för att sluta.", 
                                  lambda number: (number.lower() == "ok" and numbers)
                                  or convertToInt(number))

        if number.lower() == "ok":
            break

        number = int(number)
        numbers.append(number)

    print(numbers)
    sumOfNumbers = sum(numbers)
    averageOfNumbers = sum(numbers) / float(len(numbers))
    print("Sum:", sumOfNumbers)
    print("Average:", averageOfNumbers)


    # while True:
    #     number = input("Mata in en siffra eller 'OK' för att sluta.")
    #     if number.lower() == "ok" and numbers:
    #         break
    #     try:
    #         number = int(number)
    #         numbers.append(number)
    #         print(numbers)
    #     except:
    #         print("Input error")
    # print(numbers)
    # sumOfNumbers = sum(numbers)
    # averageOfNumbers = sum(numbers) / float(len(numbers))
    # print("Sum:", sumOfNumbers)
    # print("Average:", averageOfNumbers)

def pointToGrade():
    """
    Return the grade from given max point and your point.
    """
    def getMaxPointFromInput(inputText):
        """
        Get max point from input text.
        """
        while True:
            maxPoint = input(inputText)
            try:
                maxPoint = int(maxPoint)
                return maxPoint
            except ValueError:
                print("Du måste mata in en siffra.")

    def getYourPointFromInput(inputText):
        """
        Get your point from input text.
        """
        while True:
            yourPoint = input(inputText)
            try:
                yourPoint = int(yourPoint) 
                if yourPoint <= maxPoint and yourPoint >= 0:
                    return yourPoint
                else:
                    print("Dina poäng måste vara ett positivt tal som är lika med eller lägre än maxpoäng.")
            except ValueError:
                print("Du måste mata in en siffra.")
        
    maxPoint = getMaxPointFromInput("Ange max-poäng: ")
    yourPoint = getYourPointFromInput("Ange dina poäng: ")
    yourPointIn100 = yourPoint * 100/maxPoint

    if 90 < yourPointIn100: 
        print("Berömlig")
    elif 50 < yourPointIn100:
        print("Med beröm godkänd")
    elif 10 < yourPointIn100:
        print("Godkänd")
    elif yourPointIn100:
        print("Underkänd")

def getCircleArea():
    """
    Return the area of a circle from a given radius.
    """
    radius = getInputFromUser("Ange en radius. ", convertToInt, "Du måste mata in en siffra.")
    
    circleArea = int(radius) ** 2 * 3.14
    print("Arenan av cilkeln är " + str(circleArea) + ".")

def getHypotenuse():
    """
    Return the hypotenuse from given sides of a triangle.
    """
    side1 = getInputFromUser("Ange en siffra för ena sidan av en triangel: ", 
                             convertToInt, "Du måste mata in en siffra.")
    side2 = getInputFromUser("Ange en siffra för den andra sidan av triangeln: ", convertToInt, 
                             "Du måste mata in en siffra.")

    side1 = int(side1)
    side2 = int(side2)

    hypotenuse = round(math.sqrt(side1 ** 2 + side1 ** 2), 2)
    print("Hyotenusan är " + str(hypotenuse) + ".")

def numberComparison():
    """
    Compare a given number with the previously given number and return "Greater", "Equal" or "Less". 
    """

    def getComparisonText(number1, number2):
        """
        Get the numbers from input text.
        """
       
        try:
            if number1 and number2:
                number1 = int(number1)
                if number1 == number2:
                    return "is equal to"
                elif number1 > number2:
                    return "is less than"
                elif number1 < number2:
                    return "is greater than"                    
            else:
                return ""
        except ValueError:  
            pass

    numbers = []    
    
    i = 0
    while True:
        number = getInputFromUser("Ange ett nummer. För att sluta," 
                                  "skriv 'OK'. ", lambda number: (number.lower() == "ok" and numbers) 
                                  or convertToInt(number))
        
        if number.lower() == "ok":
            break

        number = int(number)
        numbers.append(number)      

        # if len(numbers) < 2:
        #     preNumber = ""
        # else:
        #     preNumber = numbers[numbers.index(number)-1]

        preNumber = numbers[i-1]

        if i > 0:
            print(number, getComparisonText(preNumber, number), preNumber)

        i += 1

def guessNumber():
    """
    Number-gessing game.
    """

    randomNumber = randint(1, 100)
    i = 0
    while i < 6:
        inputNumber = int(getInputFromUser("Ange ett tal: ", convertToInt, "Du måste mata in ett tal."))
        if inputNumber == randomNumber:
            print("Grattis! Du har rätt. Mis siffra:", randomNumber)
            i = None
            break

        if inputNumber < randomNumber: 
            print(inputNumber, "är lägre än Mis siffra.")            
        elif inputNumber > randomNumber: 
            print(inputNumber, "är högre än Mis siffra.")
        i += 1
    if i == 6 and i != None:
        print("Du har försökt sex gånger. Prova igen.")

def todaysMi():
    """
    Mi talks about herself
    """
    i = datetime.datetime.now()

    with open("mi_text.txt", "r") as f:
        misMood = random.choice(list(f))

    integer = randint(1, 10)
    floatNum = round(random.uniform(0.001, 10.000), 3)

    dateToday = "Idag är det %s-%s-%s." % (i.year, i.month, i.day)
    timeNow = "Klockan är %s:%s:%s nu." % (i.hour, i.minute, i.second)
    howIsMi = "Jag mår %s idag." % (misMood)
    visits = "Jag ska besöka %s företag under veckan." % (integer)
    beer = "Har druckit %s liter öl den här månaden." % (floatNum)
    
    print(dateToday, timeNow, howIsMi, visits, beer)

def shuffleWord():
    """
    Return a given word randomly shuffled
    """

    word = getInputFromUser("Mata in ett ord: ", lambda inputText: inputText)
    wordShuffled = ''.join(random.sample(word, len(word)))

    print("Omkastade ordet: ", wordShuffled)

def quote():
    """
    Return a line from a file
    """
    
    words = ["hello", "hi", "hey", "hej", "hallåj", "hejsan"]

    # Assign multiple words to "words" as a list or a tuple.

    text = getInputFromUser("Mata in en mening som innehåller något hälsningsord som 'hej', 'hi' eller 'hello' m.m. : ", lambda inputText: inputText)
    text = text.lower()

    def text_contains_any_of(text, words):
        for term in words:
            if term in text:
                return True
        return False

    if text_contains_any_of(text, words):
        with open('quotes.txt') as fh:
            line_fetched = random.choice(fh.readlines())
        print("Citat: ", line_fetched)
    else:
        quote()


def inventory():
    """
    Show, count, pick up and remove items in a list.
    """
 
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("Välj ett nummer från inventory-menyn.\n") 
    print("0) Gå tillbaka till huvudmenyn.")
    print("1) Mi ska visa vad som finns i inventoryt.")
    print("2) Mi ska berätta hur många saker hon bär på.")
    print("3) Mi ska plocka upp saker du anger.")
    print("4) Mi ska kasta bort saker du anger.")
    
    def choose():
        print("Välj ett nummber från inventrymenyn.")                    
    
    with open("inventory.txt", "r+") as f:
        items = f.read()
        items = items.replace('\n', '').replace(' ', '')
        items = items.split(",")
        last_item = items[-1]
        items_ex_last_item = items[:-1]
        print(items)

    while True:
        choice = input("--> ")

        if choice == "0":
            return

        elif choice == "1":  
            print("Mi har " + ', '.join(items_ex_last_item) + " och " + last_item + ".")
            choose()

        elif choice == "2":
            count_items =  len(items)
            print("Mi har " + str(count_items) + " varor i inventoryt.")
            choose()
            
        elif choice == "3":
            while True:
                if len(items) < 7:                  
                    pickup_item = getInputFromUser("Ange en vara du vill att Mi ska plocka upp. --> ", lambda inputText: inputText, "Mata in en vara.")
                    pickup_item = pickup_item.lower().strip()
                    items.append(pickup_item)
                    with open("inventory.txt", "w+") as f:
                        f.write(','.join(items))
                        last_item = items[-1]
                        items_ex_last_item = items[:-1]
                        
                        if len(items) == 1:
                            print("Mi har plockat upp " + pickup_item + " och nu har hon " + pickup_item + " i inventoryt.")
                        else:
                            print("Mi har plockat upp " + pickup_item + " och nu har hon " + ', '.join(items_ex_last_item) + " och " + last_item + " i inventoryt.")
                else:
                    print("Mi kan inte bära på fler saker.")
                    break
            choose()

        elif choice == "4":
            while True:
                if len(items) == 0:
                    print("Det finns inga varor i inventryt.")

                else:
                    with open("inventory.txt", "a+") as f:
                            remove_item = getInputFromUser("Ange en vara du vill att Mi ska kasta bort. --> ", lambda inputText: inputText, "Du måste mata in en vara.")
                            remove_item = remove_item.lower().strip()     

                            if remove_item in items:
                                remove_item_index = items.index(remove_item)
                                items.remove(items[remove_item_index])

                                with open("inventory.txt", "w+") as f:                      
                                        
                                    if len(items) == 0:
                                        f.write(''.join(items))
                                        print("Mi har kastat bort " + remove_item + ".") 
                                        print("Det finns inga varor i inventoryt.")
                                    
                                    else:
                                        f.write(','.join(items))

                                        if len(items) == 1:
                                            print("Mi har kastat bort " + remove_item + ".") 
                                            print("Nu har hon " + items[0] + " i inventoryt.")

                                        else:    
                                            last_item = items[-1]
                                            items_ex_last_item = items[:-1]                                    
                                            print("Mi har kastat bort " + remove_item + ".") 
                                            print("Nu har hon " + ', '.join(items_ex_last_item) + " och " + last_item + " i inventoryt.")
                            else:
                                print("Det finns ingen vara du angett i inventoryt.")  
                
        else: 
            print("Du kan bara välja mellan 0 och 4. ")


def meImage():
    """
    Store my ascii image in a separat variabel as a raw string
    """
    return r"""
    >(.)__ <(.)__ =(.)__
     (___/  (___/  (___/
    """
