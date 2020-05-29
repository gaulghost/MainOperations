import math
import re
import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

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
