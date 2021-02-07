# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:51:12 2020

@author: ma7mo
"""

def gentrator_func():
    for i in range(10):
        #yield means stop here and out the loop
        yield i 

#enter this loop and call func and it will continue where it stopped
for item in gentrator_func():
    print(item)

##########################################################
print("_________________________________________________\n")
##########################################################



def gen_func():
    for i in range(3):
        yield i
        
gen = gen_func()
print(next(gen))
print(next(gen))
print(next(gen))

##########################################################
print("_________________________________________________\n")
##########################################################

def fibon(n):
    a = b = 1
    for i in range (n):
        yield a
        a,b = b, a+b

for x in fibon(20):
    print(x)
        
