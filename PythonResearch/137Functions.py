# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:04:20 2018

@author: 1000877

Video 1.3.7: Introduction to Functions

procedual decomposition
def
return
"""
def add(a,b):
    mysum = a+b
    return mysum
'''
'''
def add_and_sub(a,b):
    mysum = a+b
    mydiff=a-b
    return (mysum,mydiff)

newadd = add
'''
two different name of the same function
'''
def modify(mylist):
    mylist[0] *=10
    
L = [1,3,5,7,9]

modify(L)

'''
def modify(mylist): 
    mylist[0] *= 10 
    return(mylist) 
L = [1, 3, 5, 7, 9] 
M = modify(L) 
M is L 
The statement is true! Note that because L is mutable, modify alters mylist directly.
'''
