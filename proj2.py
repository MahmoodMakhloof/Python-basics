# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:27:17 2020

@author: ma7mo
"""

#lambda is a qick function make
#var = lambda par1, par2 : operation
Sum = lambda x,y : x*y
print(Sum(7,8))




#filter is filtering
#filter(func , source)
Mylist =[0,1,2,3,4,5,6,7,8,9,10]
odd_numbers = list(filter(lambda x : x%2 != , Mylist))
print(odd_numbers)
even_numbers = list(filter(lambda x : x%2 ==0 ,Mylist))
print(even_numbers)




#map can apply function to all items in sequence
Mylist2 = [4,7,8,9,0,44,77,89,100]
print("squared list:",list(map(lambda x:x*x , Mylist2)))
sentence = "Hello all World"
print(list(map(lambda word:len(word),sentence.split())))


#reduce continually applies the function to the sequence
from functools import reduce
product = reduce(lambda x,y :x*y   ,   [1,2,3,4])
print('product = {}'.format(product))
