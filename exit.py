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
