# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:32:51 2022

@author: mgosh
"""

num = int(input())
count0 = 1
count1 = 1
for i in range(1,num):
    sum1 = count0 + count1
    
    count0 = count1
    count1 = sum1
    
print(count0)