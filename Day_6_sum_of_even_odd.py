# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:28:20 2022

@author: mgosh
"""

num = int(input())
even = 0
odd = 0

while(num>0):
    count = num%10
    if(count % 2 == 0):
        even += count
    else:
        odd += count
    num = num//10
print(even," ",odd)