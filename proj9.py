# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:18:16 2020

@author: ma7mo
"""

# dictionary is consist of keys & values #
d1 = {"Name":"mahmoud", "age":22,"edu":"engineer"}
print(d1)
print(d1["Name"])
print("age" in d1) #true

print("engineer" in d1 ) #false
print("engineer" in d1.values()) #true

#you can put default values for data not existed
print(d1.get("age",50))
print(d1.get("id",111))

mylist= list(d1)
print(mylist)

mylist = list(d1.values())
print(mylist)

#return list of tuples
mylist = list(d1.items())
print(mylist)

print(d1.keys())

d1 = {"name":["mahmoud","abbas"],"age":[22,55]}
print(d1["name"][1],d1["age"][1])

del d1["age"]
print(d1)

d1.clear()
print(d1) #empty dic

print(type(d1)) #dic
