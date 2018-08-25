# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:47:17 2018

@author: 1000877

1.3.1 Dynamic Typing
Review the difference between static and dynamic typing
Learn how dynamic typing in Python works for mutable and immutable objects
//
011001001
type:
    1 reading 
    2 represent
Some languages are statically typed, like C or C++,
and other languages are dynamically typed, like Python.    
//
variable
object
reference;
x=3
creat object 3
name x
reference from name to object
The variable x is referred to object 3 .
//
mutalbe objects: lists dictrionaries;
immutable: numbers strings
//
a variable can only reference an object;

"""
L1 = [1,2,3]
L2=L1
L1[0]=2
L2

L1 = [1,2,3]
M = [1,2,3]
L1 == M
L1 is M
id(L1)
id(M)
//
M=L1
L=L1
'''
M is a nickname of L
'''
M = list(L)
M = L[:]
'''
create a copy
a new list 
'''
M is L
'''
False
'''
M==L
'''
