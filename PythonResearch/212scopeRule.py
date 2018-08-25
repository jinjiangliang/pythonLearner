# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 16:25:24 2018

@author: 1000877

2.1.1: Scope Rules
Learn the LEGB rule for scope
Review some examples that demonstrate scope rules in Python
"""

'''
L stands for "local," 
E stands for "enclosing function," 
G for "global,"
and 
B stands for "built-in."
'''

def update():
    x.append(1)
    
x = [1,1]

'''
avoid
'''
'''
1)
def increment(n): 
   n += 1 
   print(n) 

n = 1 
increment(n) 
print(n) 

2 ; 1
'''

'''
def increment(n):
   n += 1
   return n

n = 1
while n < 10:
   n = increment(n)
print(n)

Explanation

return(n) will ensure that the function returns the value. This new value will be assigned to n. The while loop will continue until the condition is met.
'''