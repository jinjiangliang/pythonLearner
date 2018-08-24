# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 20:19:48 2018

@author: 1000877

1.3.5: List Comprehensions
Learn how to use a list comprehension to quickly 
and elegantly apply an operation to all items in a list

list comprehension
"""
numbers = range(10)
squares = []
for number in numbers:
    square = number**2
    squares.append(square)

'''
listcomprehension:
squares = [number**2 for number in numbers]
'''
sum([i**2 for i in range(3)])

sum([i for i in range(10) if i%2==1])
'''
Consider sum([i for i in range(10) if i%2 == 1]). This will sum all single digits as long as they are odd.

'''