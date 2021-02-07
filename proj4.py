# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 23:14:47 2020

@author: ma7mo
"""

#exception handelling

while True:
    try:
        n=input("please enter an integer:")
        n= int(n)
        break;
    except ValueError:
        print("no valid integer ! please try again")
        
        
print ("Great , you succesfully entered an integer")

#############################################################

try:
    x = float (input("your number:"))
    inverse = 1.0 /x

except ValueError:
    print("you should enter a float or an integer number")
    
except ZeroDivisionError:
    print("infinity")

finally:
    print('there may or may not have been an exception.')
