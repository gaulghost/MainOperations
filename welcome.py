import math
import re
import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

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
