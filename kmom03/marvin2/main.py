#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mi with a simple menu to start up with.
Mi doesnt do anything, just presents a menu with some choices.
You should add functinoality to Mi.

"""
import marvin 
import sys

# Python 2.x.x "input" command will evaluate input, which is insecure and a different behavior from Python 3.x.x
if sys.version_info.major != 3:
    print("Please run program with Python v3.")
    sys.exit(0)

def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed. 
    It should check the choice done by the user and call a appropriate 
    function.
    """
    while True:
        menu()
        choice = input("--> ")
        if choice == "q":
            print("Hejdå!")
            return  
        elif choice == "0":
            presentation()      
        elif choice == "1":
            yearToSecond()
        elif choice == "2":
            weightMoon()
        elif choice == "3":
            minutesToHours()
        elif choice == "4":
            celciusToFahrenheit()   
        elif choice == "5":
            wordMultiply()
        elif choice == "6":
            randomNumbers()
        elif choice == "7":
            sumAndAverage()
        elif choice == "8":
            pointToGrade()
        elif choice == "9":
            getCircleArea()
        elif choice == "10":
            getHypotenuse()
        elif choice == "11":
            numberComparison()
        elif choice == "12":
            guessNumber()
        elif choice == "13":
            todaysMi()
        elif choice == "14":
            shuffleWord()
        else:
            print("Du kan bara välja från menyn . ")          
            
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
