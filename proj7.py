# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:03:00 2020

@author: ma7mo
"""

# Tuples is faster than lists but is fixed data #
mylist = ['a', 'b','c']
t1 = ('x','y','z')
t2 = ('j','k')

mytuple = tuple(mylist) + t2 + t1
print(mytuple)

del (mytuple)
#error because mytuple is deleted
print(mytuple)