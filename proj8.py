# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:09:01 2020

@author: ma7mo
"""

# Sets is a sequence of unique values 
# unique means don't repeated data
# Sets are faster than lists and mathematical operation can be applies

s1 = {"apple", 1,"apple",1,1,"apple" ,"carrot",(1,2),(1,2)}
print(s1)

s1 = set("abcdef")
s2 = set("efghi")
#ef is common 
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)