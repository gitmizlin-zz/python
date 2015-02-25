#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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