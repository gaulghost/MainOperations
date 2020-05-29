import math
import re
import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

def mexp() :
    print('''Which mathematical expression would you like to preform first
    1. Power / 1 / "**"
    2. Division / 2 / "/"
    3. Multipication / 3 / "*"
    4. Substraction / 4 / "-"
    5. Addition / 5 / "+"
    6. Remainder / 6 / "%"
    7. Logarithm / 7 / log
    8. Cosine / 8 / cos
    9. Sine / 9 / sin
    10. Tangent / 10 / tan\n''')
    firstnum = None
    secondnum = None
    operand = None
    loop1var = 0
    while True:
        operand = input("Operation you want to preform \n")
        if operand.lower() == "sine" or operand.lower() == "sin" or operand.lower() == "tan" or operand.lower() == "tangent" or operand.lower() == "cos" or operand.lower() == "cosine" or operand == "8" or operand == "9" or operand == "10"  :
            theta = input('''1. Theta in radians (Default)
2. Theta in degrees \n''')
            try :
                if loop1var == 0 :
                    firstnum = float(input("Enter the first num \n"))
                else :
                    firstnum = output
            except :
                exiter()
                continue
            if theta.lower() == "degrees" or theta.lower() == "degree" :
                firstnum = (180 / math.pi) * firstnum
            if operand.lower() == "cosine" or operand.lower() == "cos" or operand == "8" :
                output = math.cos(firstnum)
            elif operand.lower() == "sine" or operand.lower() == "sin" or operand == "9" :
                output = math.sin(firstnum)
            else :
                output = math.tan(firstnum)
        elif operand.lower() == "power" or operand == "1" or operand == "**" or operand.lower() == "division" or operand == "2" or operand == "/" or operand.lower() == "multipication" or operand == "3" or operand == "*" or operand.lower() == "substraction" or operand == "4" or operand == "-" or operand.lower() == "addition" or operand == "5" or operand == "+" or operand.lower() == "remainder" or operand == "6" or operand == "%" or operand.lower() == "logarithm" or operand == "0" or operand == "log" :
            try :
                if loop1var == 0 :
                    firstnum = float(input("Enter the first num \n"))
                    secondnum = float(input("Enter the second num \n"))
                else :
                    firstnum = output
                    secondnum = float(input("Enter the second num \n"))
            except :
                exiter()
                continue
            if operand.lower() == "power" or operand == "1" or operand == "**" :
                output = firstnum ** secondnum
            elif operand.lower() == "division" or operand == "2" or operand == "/" :
                output = firstnum / secondnum
            elif operand.lower() == "multipication" or operand == "3" or operand == "*":
                output = firstnum * secondnum
            elif operand.lower() == "substraction" or operand == "4" or operand == "-":
                output = firstnum - secondnum
            elif operand.lower() == "addition" or operand == "5" or operand == "+":
                output = firstnum + secondnum
            elif operand.lower() == "remainder" or operand == "6" or operand == "%":
                output = firstnum % secondnum
            else :
                output = math.log(firstnum , secondnum)
        else :
            exiter()
            continue
        print("Output is : ",output)
        loop1var = loop1var + 1
        # fcalc - futher calculate
        fcalc = input("Want to further calculate on the output? If no type done else press any key to continue\n")
        if fcalc.lower() == "done" :
            break
    print("Your final output is :",output)
