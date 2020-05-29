import math
import re
import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl


from exit import exiter
from welcome import Welcome
from calc import mexp
from compNum import mel
from wordFilter import wordfilter
from compStrChar import comparechar,comparestr


Welcome()
while True :
    print('''\nWhat would you like to do ?
    1. Would like to preform mathematical operations
    2. Would like to preform logical operations
    3. Would like to preform operations on some data \n''')
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
