import math
import re
import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

def exiter() :
    print("You have entered wrong input")
    exiter = input("If you would like to exit type yes/y or press any key\n")
    if exiter.lower() == "yes" or exiter.lower() == "y":
        exit()
def Welcome() :
    while True :
        lang = input("Which lang do u understand : en/fr/es\n")
        if lang == "en" :
            greet = "Hello"
            break
        elif lang == "fr" :
            greet = "Bonjour"
            break
        elif lang == "es" :
            greet = "Hola"
            break
        else :
            exiter()
            continue
    if lang == "en" :
        user = input("what is your name\n")
        for i in range(3,0) :
            print(i)
        n = print(greet,user,"Welcome to my world of python")
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
def comparechar() :
    lst1 = list(range(65,91))
    lst2 = list(range(97,123))
    flst = lst1 + lst2
    greatestchar = None
    smallestchar = None
    x = 0
    nnum = None
    print('Write $$done&&$ to finish entering characters')
    while True:
        nchar = input('Enter a characters: ')
        if nchar == '$$done&&$' :
            break
        for word in nchar :
            asci = ord(word)
            if asci not in flst :
                exiter()
                continue
        if x == 0 :
            greatestchar = nchar
            smallestchar = nchar
        if greatestchar < nchar :
            greatestchar = nchar
        if smallestchar > nchar :
            smallestchar = nchar
        x = x+1
    print("Greatest is", greatestchar)
    print("Smallest is", smallestchar)
def comparestr() :
    largeststr = None
    smalleststr = None
    x = 0
    print('Write $$done&&$ to finish entering strings')
    while True:
        nstr = input('Enter a String: ')
        if nstr == '$$done&&$' :
            break
        if x == 0 :
            largeststr = nstr
            smalleststr = nstr
        if largeststr < nstr :
            largeststr = nstr
        if smalleststr > nstr :
            smalleststr = nstr
        x = x+1
    print("Largest is", largeststr)
    print("smallest is", smalleststr)
def mel():
    count = 0
    sum = 0
    mid = 0
    mean = None
    median = None
    largest = None
    smallest = None
    appearance = dict()
    numlist = []
    mode = 0
    i = 0
    wtp = []
    print("Write done to stop entering number")
    while True:
        str = input('Enter a number: ')
        if str.lower() == 'done' :
            break
        try :
            number = int(str)
        except :
            exiter()
            continue
        numlist.append(number)
        count = count + 1
        sum = sum + number
    mid = int(count/2)
    mean = sum/count
    for number in numlist :
        i += 1
        if i == mid :
            median = number
        if i == 1 :
            largest = number
            smallest = number
        if largest < number :
            largest = number
        if smallest > number :
            smallest = number
        appearance[number] = appearance.get(number , 0) + 1
    for key in appearance :
        if mode < appearance[key] :
            mode = appearance[key]
            modenum = key
    wtp = input('''What do you want to find ?
    1. Total Count
    2. Sum
    3. Mean / Average
    4. Median
    5. Mode
    6. Largest
    7. Smallest
    8. Histogram \n''')
    for i in wtp :
        if i == "1" :
            print("Count", count)
        if i == "2" :
            print("Sum", sum)
        if i == "3" :
            print("Mean/average", mean)
        if i == "4" :
            print("Median", median)
        if i == "5" :
            print("Mode (number,appearance)", modenum, mode)
        if i == "6" :
            print("Largest", largest)
        if i == "7" :
            print("Smallest", smallest)
        if i == "8" :
            print("Histogram", appearance)
def wordfilter(user):
    fhand = open(user)

    lst1 = list(range(65,91))
    lst2 = list(range(97,123))
    flst = lst1 + lst2

    validword2 = list()
    strings = list()
    invalidword = list()
    validword = list()

    for line in fhand :
        line = line.rstrip()
        x = re.findall('\s([a-zA-Z]+)\.\s', line)
        y = re.findall('\s([a-zA-Z]+),\s', line)
        z = re.findall('([a-zA-Z]+),\s', line)
        w = re.findall('([a-zA-Z]+)\.\s', line)
        if x is not None :
            for word in x:
                validword2.append(word)
        if y is not None :
            for word in y:
                validword2.append(word)
        if z is not None :
            for word in z:
                validword2.append(word)
        if w is not None :
            for word in w:
                validword2.append(word)
        line = line.split()
        for word in line :
            strings.append(word)

    for string in strings :
        for letter in string :
            if ord(letter) not in flst :
                invalidword.append(string)

    validword = set(strings)-set(invalidword)

    for word in validword2 :
            validword.add(word)

    print(validword)
    print(len(validword))

Welcome()
print('''What would you like to do ?
1. Would like to preform mathematical operations
2. Would like to preform logical operations
3. Would like to preform operations on some data \n''')
while True :
    # wltp - Would like to preform
    wltp = input ("Select one of the above options \n")
    if wltp == "1" :
        print('''1. Would like to use calculator
2. Compare list of numbers \n''')
        # wltp2 - Would like to preform 2
        wltp2 = input ("Select one of the above options\n")
        if wltp2 == "1" :
            mexp()
        elif wltp2 == "2" :
            mel()
    elif wltp == "2" :
        # wltp3 - Would like to preform 3
        wltp3 = input('''1. Compare list of numbers ?
2. Compare list of characters
3. Compare list of strings \n''')
        if wltp3 == "1" :
            mel()
        elif wltp3 == "2" :
            comparechar()
        elif wltp3 == "3" :
            comparestr()
        else :
            exiter()
            continue
    elif wltp == "3" :
        wltp4 = input('''1. Filtering out words from expressions and numbers.
More exciting features coming\n''')
        if wltp4 == "1" :
            user = input("enter the file name\n")
            try :
                wordfilter(user)
            except :
                print('You have entered inexisting file')
                exiter()
    else :
        exiter()
        continue
