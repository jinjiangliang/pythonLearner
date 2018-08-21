# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:14:09 2018

@author: 1000877

Video 1.2.3: Tuples
immutable;
"""
T = (1,3,5,7)
len(T)
T+(9,11)
T[1]

'''
pack

x=12.23
y=23.34
coordinate = (x,y)
type(coordinate)

unpack
(c1,c2) = coordinate

c1
c2
'''
coordinates = [(1,1), (2,2)]
for (x,y) in coordinates:
    print(x,y)
    
for x,y in coordinates:
    print (x,y)

c=(2,3)
type(c)

c = (2)    
type(c)    

'''
tuple with 1 element
c = (2,)
type(c)    
c= 2,

This is impossible: tuples are immutable, 
so they can't be edited after they’ve been created.

Consider x=(1,2,3) . 
Use the count method to count the number of 3 s in x .

 x.count(3)
 sum(x)
 
 type((2,)) correct
 '''
 