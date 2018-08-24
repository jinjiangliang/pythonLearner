# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:48:12 2018

@author: 1000877

exercise 2
"""

'''
Consider a circle enclosed by a square. The ratio of their areas is pi / 4. In this six-part exercise, 
we will find a way to approximate this value.
2a
Using the math library, calculate and print the value of pi / 4.
'''
import math
print(math.pi/4)

'''
2b
Using random.uniform(), 
create a function rand() that 
generates a single float between -1 and 1.
Call rand() once. 
So we can check your solution, 
we will use random.seed() to 
fix the value called by your function.
'''
import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

def rand():
   # define `rand` here!
   random.uniform(-1,1)
   
rand()

'''
2c
The distance between two points x and y is the square root of the sum of squared differences along each dimension of x and y. Create a function distance(x, y) that takes two vectors and outputs the distance between them. Use your function to find the distance between x=(0,0) and y=(1,1).
Print your answer.
'''
import math

def distance(x, y):
   # define your function here!
   import math

def distance(x, y):
   # define your function here!
    distance_square = 0
    z=len(x)
    for i in range(z):
        difference = (x[i]-y[i])**2
        distance_square += difference
    distance = distance_square**0.5
    return distance
    
x =(0,0)
y = (1,1)  

print(distance(x,y))

'''
note, we need :
    after def, for and if
'''
import random, math

random.seed(1)

def in_circle(x, origin = [0]*2):
   # Define your function here!
    if distance(x,origin)<1:
        return True
    else:
        return False

print(in_circle((1,1)))

'''
2e
Create a list of R=10000 booleans called inside that determines whether each point in x falls within the unit circle centered at (0,0). Make sure to use in_circle.
Find the proportion of points within the circle by summing the count of True in inside, and dividing by R.
Print your answer. This proportion is an estimate of the ratio of the two areas!
'''
R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    # append inside here!
    inside.append(in_circle(point))

print(sum(inside) / R)
'''
2f
'''
print(sum(inside) / R - math.pi/4)
