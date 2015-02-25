#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mi with a simple menu to start up with.
Mi doesnt do anything, just presents a menu with some choices.
You should add functinoality to Mi.

"""

import sys
import math
from random import randint
import random
import datetime
import marvin

# Python 2.x.x "input" command will evaluate input, which is insecure and a different behavior from Python 3.x.x
if sys.version_info.major != 3:
    print("Please run program with Python v3.")
    sys.exit(0)

def meImage():
    """
    Store my ascii image in a separat variabel as a raw string
    """
    return r"""
    >(.)__ <(.)__ =(.)__
     (___/  (___/  (___/
    """

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
    print("q) Quit.")

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
