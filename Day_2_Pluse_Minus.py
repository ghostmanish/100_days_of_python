# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 11:11:15 2021

@author: Manish Kumar Goswami

"""

num = int(input())
l1 = []
sum1 = 0

for i in range(0,num):
    el = int(input())
    l1.append(el)
    
countp = 0
countn = 0
countz = 0
for j in l1:
    if j>0:
        countp +=1
    elif j<0:
        countn += 1
    else:
        countz += 1
 
print(format(countp/num,'.6f'))
print(format(countn/num,'.6f'))
print(format(countz/num,'.6f'))
