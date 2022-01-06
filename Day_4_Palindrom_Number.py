# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:19:19 2022

@author: mgosh
"""

def checkPalindrome(num):
    temp = 0
    temp1 = num 
    while(temp1>0):
        count = temp1%10
        temp = temp*10 + count
        temp1 = temp1//10
    if temp == num:
        print(temp)
        return True
    else:
        print(temp)
        return False
#Implement Your Code Here
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
