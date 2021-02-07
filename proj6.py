# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:25:53 2020

@author: ma7mo
"""

#list#

mylist = [100,6,56,89,43,11,99]
print(mylist)


mylist.append(999)
print(mylist)

mylist.extend([66,8,9])
print(mylist)

mylist.sort()
print(mylist)

mylist.pop()
print(mylist)

mylist.pop(5)
print(mylist)

del mylist[3]
print(mylist)

mylist.remove(100)
print(mylist)

mylist = [x**2 for x in range(5)]
print(mylist)

mylist= list(map(lambda x: x**2 , range(10)))
print(mylist)

print(len(mylist))
print(max(mylist))
print(min(mylist))
print(sum(mylist))
print(sorted(mylist))

s = "apple"
mylist= list(s)
print(mylist)

ss = "i love programming"
mylist = ss.split(" ")
print(mylist)

mylist =[1,3,1,6,1]
print(mylist.count(1))
print(mylist.index(3))

mylist.reverse()
print(mylist)

mylist.insert(2,"hhh")
print(mylist)
