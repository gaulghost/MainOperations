import math
import re
import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

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
