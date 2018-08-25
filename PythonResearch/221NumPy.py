# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 19:36:30 2018

@author: 1000877

2.2.1: Introduction to NumPy Arrays
Learn how to import NumPy
Learn how to create simple NumPy arrays, including vectors and matrices of zeros and ones

n-dimentional;
C, C++
linear algebra
numpy.org;

"""

import numpy as np
zero_vector = np.zeros(5)
zero_matrix = np.zeros((5,3))

x = np.array([1,2,3])
y = np.array([3,6,9])

[[1,3],[5,9]]
A = np.array([[1,3],[5,9]])
A.transpose()
#Transpose

'''
True or False: a numpy array's length may be modified after being created.
False
//
numpy.array([0., 0., 0., 0., 0.])
numpy.zeros(5)
//
Consider the following code:

x = numpy.array([[3,6],[5,7]]) 
y = x.transpose() 
print(y) 
What does this print?
array([[3 5],[6 7]])
'''
