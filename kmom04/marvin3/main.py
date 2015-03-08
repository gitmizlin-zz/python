#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mi with a simple menu to start up with.
Mi doesnt do anything, just presents a menu with some choices.
You should add functinoality to Mi.

"""
import marvin

# Python 2.x.x "input" command will evaluate input, which is insecure and a different behavior from Python 3.x.x
# if sys.version_info.major != 3:   
#     print("Please run program with Python v3.")
#     sys.exit(0)

def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed. 
    It should check the choice done by the user and call a appropriate 
    function.
    """
    while True:
        marvin.menu()
        choice = input("--> ")
        if choice == "q":
            print("Hejdå!")
            return  
        elif choice == "0":
            marvin.presentation()
        elif choice == "1":
            marvin.yearToSecond()
        elif choice == "2":
            marvin.weightMoon()
        elif choice == "3":
            marvin.minutesToHours()
        elif choice == "4":
            marvin.celciusToFahrenheit()   
        elif choice == "5": 
            marvin.wordMultiply()
        elif choice == "6":
            marvin.randomNumbers()
        elif choice == "7":
            marvin.sumAndAverage()
        elif choice == "8":
            marvin.pointToGrade()
        elif choice == "9":
            marvin.getCircleArea()
        elif choice == "10":
            marvin.getHypotenuse()
        elif choice == "11":
            marvin.numberComparison()
        elif choice == "12":
            marvin.guessNumber()
        elif choice == "13":
            marvin.todaysMi()
        elif choice == "14":
            marvin.shuffleWord()
        elif choice == "15":
            marvin.quote()
        elif choice == "16":
            marvin.inventory()
        else:
            print("Du kan bara välja från menyn . ")          
            
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
