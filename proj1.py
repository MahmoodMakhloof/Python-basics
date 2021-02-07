# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:04:31 2020

@author: ma7mo
"""


def main():
    
    x= int(input("enter x :"))
    y= int(input("enter y :"))
    
    print("Max of {} and {} is {}".format(x,y,Max(x,y)))
    
    
    L = [2,5,6,7,8,9]
    print(isExisted(7,L))
    
    
def Max(x,y):
    if x>y:
        return x
    elif x<y:
        return y
        

def Min(x,y):
    Min = x if(x<y) else y
    return Min

def isExisted(x,List):
    if x in List:
        return True
    else:
        return False


if __name__=="__main__":main()