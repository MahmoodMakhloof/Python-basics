# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 23:25:04 2020

@author: ma7mo
"""

def factorial (n):
    if n==1:
        return n
    else:
        return n * factorial(n-1)
    
print(factorial(100))