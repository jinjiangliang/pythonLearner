# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:17:25 2018

@author: 1000877

Exercise 3a
A list of numbers can be very unsmooth, 
meaning very high numbers can be right next to very low numbers. 
This list may represent a smooth path in reality 
that is masked with random noise 
(for example, satellite trajectories with inaccurate transmission).
 One way to smooth the values in the list is to 
 replace each value with the average of each value's neighbors, 
 including the value itself.
 
 Write a function moving_window_average(x, n_neighbors) that takes a list x and the number of neighbors n_neighbors on either side of a given member of the list to consider.
For each value in x, moving_window_average(x, n_neighbors) computes the average of that value's neighbors, where neighbors includes the value itself.
moving_window_average should return a list of averaged values that is the same length as the original list.
If there are not enough neighbors (for cases near the edge), substitute the original value as many times as there are missing neighbors.
Use your function to find the moving window sum of x=[0,10,5,3,1,5] and n_neighbors=1.
"""

import random

random.seed(1)

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    y = list()
    width = n_neighbors*2 + 1
    '''
    If there are not enough neighbors (for cases near the edge), substitute the original value as many times as there are missing neighbors.
    '''
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    for i in range(n):
        y.append(sum(x[i:i+width])/width)
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    return y
    
x=[0,10,5,3,1,5]
print(moving_window_average(x, 1))

'''
Compute and store R=1000 random values from 0-1 as x.
moving_window_average(x, n_neighbors) is pre-loaded into memory from 3a. Compute the moving window average for x for values of n_neighbors ranging from 1 to 9 inclusive.
Store x as well as each of these averages as consecutive lists in a list called Y.
'''
import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.
    
# write your code here!
R = 1000;
x = []
for i in range(R):
    x.append(random.uniform(0,1))

Y = []
Y.append(x)

for i in range(1,10):
    Y.append(moving_window_average(x,i))
    
'''
3c
moving_window_average(x, n_neighbors=2) and Y are already loaded into memory. For each list in Y, calculate and store the range (the maximum minus the minimum) in a new list ranges.
Print your answer. 
As the window width increases, 
does the range of each list increase or decrease? 
Why do you think that is?
'''
# write your code here!
ranges = list()
for i in range(len(Y)):
    ranges.append(max(Y[i])-min(Y[i]))

print(ranges)








