# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 23:54:09 2021

@author: Manish Kumar Goswami
"""

import re
import pyfiglet
from datetime import datetime

#Banner Of my Calculator

banner = pyfiglet.figlet_format("MKG CALCULATOR")
print(banner)

#Adding Banner 

print("-" * 100)
print("Tool created by Manish Kumar Goswami")
print("Calculator Started At: "+ str(datetime.now()))
print("-" * 100)


print("\n")
print("\n")
print("\n")


print("Type Q to quit and C to clear all the values")

#Initilisation Variable

previos_value = 0
run =True

#Function for calcualtor

def calcualtor():
    global run
    global previos_value
    
    if previos_value ==0:
        equation = input("Enter your equation")
    else:
        equation = input(str(previos_value))
    
    if equation == "Q" or equation == "q":
        print("Good Bye See You Soon")
        print("\U0001F917 \U0001F917 \U0001F917")
        run = False
    elif equation == "C" or equation == "c":
        previos_value = 0
    else:
        equation = re.sub('[a-zA-z,.:;" "{}?\@`~#$_]','',equation)
        
        if previos_value == 0:
            previos_value = eval(equation)
        else:
            previos_value = eval(str(previos_value) + equation)
            
#end of function

#Starting of loop for infinite time.

while run:
    calcualtor()
    